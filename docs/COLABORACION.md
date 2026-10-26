# Cómo publicar la colaboración

El repositorio local ya tiene la línea base en `main`, una rama por integrante y la
versión integrada en `solucion`.

## 1. Subir todo

```bash
# desde la carpeta del proyecto, con el remoto del repo de la organización
git remote add origin https://github.com/UTEC-AII/trabajo-final-algoritmos.git
git push -u origin main
git push origin feat/s1-ingesta-dedup fix/s3-matriz-grafo fix/s6-ventana feat/s7-experimentos
git push origin solucion
```

## 2. Abrir los pull requests

Cada rama se abre contra `main`. El autor no revisa su propio PR: lo revisa otro
integrante y, si toca una estructura, su dueño según `.github/CODEOWNERS`.

```bash
gh pr create --base main --head feat/s1-ingesta-dedup \
  --title "S0/S1: cola acotada y deduplicación con conjunto hash" \
  --body "Cierra el punto 2 y 3 de la revisión. Ver tests/test_structures.py."

gh pr create --base main --head fix/s3-matriz-grafo \
  --title "S3/S4/S5: corrige la corrupción de la matriz y del grafo" \
  --body "La celda y la arista pasan a ser pares; el B+Tree expone sus métricas."

gh pr create --base main --head fix/s6-ventana \
  --title "S6: ventana móvil sin marcas permanentes" \
  --body "El umbral se evalúa siempre sobre los últimos 10 minutos."

gh pr create --base main --head feat/s7-experimentos \
  --title "S7 y experimentos: memoria pico de todas las estructuras" \
  --body "Cierra el requisito de memoria con tracemalloc."
```

## 3. Cerrar la colaboración

Al mergear los cuatro PR, `main` queda igual a `solucion`. Para comprobarlo:

```bash
git diff main solucion --stat   # debe quedar vacío tras el último merge
```

## 4. Reglas

- Nadie hace push directo a `main`; todo entra por PR con una revisión.
- Si un PR cambia una cifra del informe, en el mismo PR van el CSV regenerado,
  el `.tex` y el PDF recompilado.
- Cada integrante debe poder explicar el código de su rama: la sustentación es
  individual y vale 6 puntos.
