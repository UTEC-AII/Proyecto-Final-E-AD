"""S1: deduplicación por búsqueda binaria en corridas ordenadas frente a un conjunto hash.

Recorre el stream de 10M eventos en lotes de 5,000 y pasa cada lote por las dos
variantes de la ventana de 500K ids. Comprueba que la salida sea idéntica lote
por lote y mide el tiempo de cada una.

    python bench/bench_s1_dedup.py --data data/rees46_10000000
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
import time
from collections import deque

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from eda.pipeline.events import iter_events  # noqa: E402
from eda.pipeline.stages import Preprocessor  # noqa: E402
from eda.structures import HashSet, merge_sort  # noqa: E402


class HashSetPreprocessor(Preprocessor):
    """Variante de referencia: la ventana es un conjunto hash con anillo de expiración."""

    def __init__(self, window_ids: int = 500_000) -> None:
        super().__init__(window_ids)
        self.seen = HashSet(max(16, window_ids * 2))
        self.ring: deque = deque()

    def process(self, batch):
        clean = [e for e in batch if self._valid(e)]
        self.invalid += len(batch) - len(clean)
        for e in clean:
            e.brand = (e.brand or "generic").strip().lower()
            e.category_code = (e.category_code or "unknown").strip().lower()
            e.search_query = (e.search_query or "").strip().lower()
            e.price = round(float(e.price), 2)
        out, last = [], None
        for e in merge_sort(clean, key=lambda e: e.event_id):
            if e.event_id == last or e.event_id in self.seen:
                self._drop(e)
                continue
            last = e.event_id
            self.seen.add(e.event_id)
            self.ring.append(e.event_id)
            if len(self.ring) > self.window_ids:
                self.seen.discard(self.ring.popleft())
            out.append(e)
        return merge_sort(out, key=lambda e: e.ts)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/rees46_10000000")
    ap.add_argument("--batch", type=int, default=5_000)
    ap.add_argument("--out", default="results/bench/s1_dedup.csv")
    a = ap.parse_args()
    variants = {"busqueda_binaria": Preprocessor(), "conjunto_hash": HashSetPreprocessor()}
    secs = dict.fromkeys(variants, 0.0)
    batches = mismatched = 0

    def step(batch):
        nonlocal batches, mismatched
        outs = {}
        for name, s1 in variants.items():
            t = time.perf_counter()
            outs[name] = [e.event_id for e in s1.process(list(batch))]
            secs[name] += time.perf_counter() - t
        batches += 1
        mismatched += outs["busqueda_binaria"] != outs["conjunto_hash"]

    batch = []
    for e in iter_events(os.path.join(a.data, "events.parquet")):
        batch.append(e)
        if len(batch) == a.batch:
            step(batch)
            batch = []
    if batch:
        step(batch)
    rows = [{"variante": name, "lotes": batches, "lotes_distintos": mismatched, "segundos": round(secs[name], 2),
             "duplicados": s1.duplicates, "duplicados_reales": s1.dup_true_positive} for name, s1 in variants.items()]
    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(r)


if __name__ == "__main__":
    main()
