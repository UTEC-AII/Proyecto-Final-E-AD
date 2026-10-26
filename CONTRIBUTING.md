# Cómo colaboramos

## Regla base

`main` siempre corre. Nadie hace push directo a `main`: todo entra por Pull Request con al menos una revisión de otro integrante. Esto es lo que deja el historial de contribución verificable que pide el curso.

## Flujo

1. Toma un issue de los que salen de `Puntos_a_Mejorar.md` y asígnalo a ti.
2. Crea la rama: `fix/s6-cooldown-ventana`, `feat/s1-hash-set-ventana`, `docs/informe-seccion-3`.
3. Commit con el prefijo de la etapa:
   ```text
   fix(s6): levanta la marca de la tarjeta al caer bajo el umbral

   El umbral se evaluaba una vez y la tarjeta quedaba bloqueada para
   siempre. Ahora la marca expira cuando el conteo de la ventana baja.
   ```
4. Push y Pull Request con el template.
5. Otro integrante revisa (no el autor). Si toca una estructura, la revisa su dueño según `CODEOWNERS`.
6. Squash merge. Borrar la rama.

## Convención de commits

`tipo(etapa): descripción en imperativo`

- `tipo`: `feat`, `fix`, `docs`, `test`, `bench`.
- `etapa`: de `s0` a `s9`, `informe` o `repo`.
- Ejemplo: `bench(s7): reporta recall@10 global además del condicional`.

## Regla de oro del informe

Si un PR cambia una cifra que aparece en el PDF (tiempo, recall, memoria, número de eventos), en el mismo PR van:

1. el CSV regenerado en `results/bench/`,
2. el número actualizado en `report/informe.tex`,
3. el PDF recompilado.

Si no, en dos semanas el informe y los datos no van a coincidir.

## Entorno local

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q                                  # 20 pruebas
python scripts/prepare_data.py --events 200000
python scripts/run_pipeline.py --data data/synthetic_200000 --refresh 50000
```

`data/`, `.venv/` y `*.bpt` están ignorados: no se suben.
