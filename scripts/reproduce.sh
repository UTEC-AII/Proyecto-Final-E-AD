#!/usr/bin/env bash
# Reproduce la entrega completa en el orden en que se generaron los resultados.
# Requiere: 2019-Oct.csv de REES46 en data/raw/ y un entorno con requirements.txt.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== 1/4  Datos (10M eventos reales + componente sintetico)"
python scripts/prepare_data.py --source rees46 --events 10000000

echo "== 2/4  Pipeline de punta a punta (5 refrescos, ~5 min en un Apple M5)"
python scripts/run_pipeline.py --data data/rees46_10000000 \
    --batch 5000 --refresh 2000000 --out results/demo/summary_10M.json

echo "== 3/4  Experimentos (1K a 10M) y figuras"
python bench/run_benchmarks.py
python bench/plots.py

echo "== 4/4  Informe"
cd report && pdflatex -interaction=nonstopmode Proyecto_Final_Grupo2.tex >/dev/null
pdflatex -interaction=nonstopmode Proyecto_Final_Grupo2.tex >/dev/null
cd ..

echo "Listo: results/, report/figures/ y report/Proyecto_Final_Grupo2.pdf"
