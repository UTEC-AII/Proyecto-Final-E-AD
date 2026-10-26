# Historial de colaboración

El proyecto se integró con pull requests: cada integrante abrió el suyo desde su
cuenta, otro lo revisó y `main` solo recibió cambios aprobados. Son siete PRs,
seis mergeados y uno reemplazado por su repetición.

| PR | Autor | Rama | Qué cambió | Líneas | Archivos |
|---|---|---|---|---|---|
| [#1](https://github.com/UTEC-AII/Proyecto-Final-E-AD/pull/1) | sebastian-rgv | `feat/s1-ingesta-dedup` | S0 con cola de un lote y contador de rechazos; S1 con deduplicación propia | +21 / −14 | 2 |
| [#2](https://github.com/UTEC-AII/Proyecto-Final-E-AD/pull/2) | sebastian-rgv | `docs/entrega-final` | Informe en LaTeX, notebook ejecutado, láminas, README, licencia y `reproduce.sh` | +5,024 / −44 | 18 |
| [#3](https://github.com/UTEC-AII/Proyecto-Final-E-AD/pull/3) | dantebarreto-gif | `fix/s3-matriz-grafo` | Celda de la matriz como par (fila, columna), arista como par (u, v) y métricas del B+Tree | +35 / −21 | 4 |
| [#4](https://github.com/UTEC-AII/Proyecto-Final-E-AD/pull/4) | clintonchulluncuy-pixel | `fix/s6-ventana` | S6 evalúa el umbral sobre la ventana móvil, sin marcas permanentes | +15 / −4 | 1 |
| [#5](https://github.com/UTEC-AII/Proyecto-Final-E-AD/pull/5) | rhilarioorihuela | `feat/s7-experimentos` | Memoria actual y pico de las ocho estructuras con `tracemalloc` | +17 / −5 | 1 |
| [#6](https://github.com/UTEC-AII/Proyecto-Final-E-AD/pull/6) | dantebarreto-gif | `revision-coherencia` | S1 con búsqueda binaria y coherencia del informe, las láminas y el README. Cerrado sin mergear | +182 / −51 | 12 |
| [#7](https://github.com/UTEC-AII/Proyecto-Final-E-AD/pull/7) | dantebarreto-gif | `revision-coherencia` | El mismo cambio que #6, mergeado | +182 / −51 | 12 |

## Dos aclaraciones

**S1 terminó con búsqueda binaria, no con conjunto hash.** El PR #1 introdujo una
deduplicación con conjunto hash, pero la etapa 1 del enunciado pide ordenación y
búsqueda binaria. El PR #7 la reemplazó por un anillo de corridas ordenadas con
búsqueda binaria vectorizada, que es lo que describen el informe y las láminas.
El resultado es el mismo: los 151,081 duplicados se eliminan igual.

**El PR #6 quedó cerrado sin mergear** porque Dante abrió dos veces el mismo
cambio; el #7 es el que entró a `main`. No hay pérdida de contenido.

## Cómo se trabajó

- Cada PR lo abrió su autor desde su cuenta; ninguno se autoaprobó sin revisión.
- El flujo de pruebas corre en cada PR: 20 pruebas automáticas.
- Los cambios que tocan una estructura los revisó su responsable según
  `.github/CODEOWNERS`.
- Si un PR cambiaba una cifra del informe, en el mismo PR iban el CSV, el `.tex`
  y el PDF recompilado.

## Estado final

`main` y la etiqueta `v1.0-entrega` apuntan al mismo commit. Las ramas de trabajo
quedan en el repositorio como registro de cada aporte.
