# Modelo de datos y reglas de cálculo

Estado: **verificado contra los datos del repositorio** en la fecha de la última
entrada de la [bitácora](BITACORA.md). Cada afirmación lleva la evidencia con la
que se comprobó. Lo que no se ha podido verificar está marcado como
**`[NO VERIFICADO]`** y no debe usarse como regla hasta confirmarlo.

## 1. Ficheros y cadena de derivación

Todo el dato vive en `datos/`. El microsite lo lee por ruta relativa
(`microsite.html:301` → `var BASE='./datos/'`), así que un cambio en `datos/`
publicado en la rama que sirve la web es un cambio en producción.

| Fichero | Papel | Grano |
|---|---|---|
| `TodasDimensiones.xlsx` | Origen externo. Contiene las escalas de puntos y los maestros | hojas |
| `calendario.json` | Maestro de torneos: tipo, campo, par, si está jugado | torneo |
| `jugadores.json` | Maestro de jugadores por temporada: socio / invitado / no participa | jugador·temporada |
| `resultados.json` | Golpe a golpe, hoyo por hoyo | jugador·torneo·hoyo |
| `tarjetas_YYYY.json` | Tarjeta por jugador y **ronda**, con el detalle de los 18 hoyos | jugador·ronda |
| `clasificacion_YYYY.json` | Resultado por jugador y **torneo**, con posición y puntos | jugador·torneo |
| `clas_matrix_YYYY.json` | Clasificación general de la temporada | jugador·temporada |
| `equipos_clasificacion_YYYY.json` | Clasificación por equipos, por torneo y de temporada | equipo |
| `handicaps.json` | Histórico de handicaps | jugador·fecha |
| `campos.json`, `estadisticas.json` | Datos de campo y estadística agregada | campo |
| `csc.json` | Liga Clubes Sin Campo, ajena a la liga interna | modalidad |

Cobertura comprobada:

- `tarjetas_*` y `clasificacion_*`: 2021 a 2026.
- `clas_matrix_*` y `equipos_clasificacion_*`: 2024 a 2026 (equipos) y 2021 a 2026 (matrix).
- `jugadores.json`: temporadas **2020 a 2025 únicamente**. No hay ninguna fila de 2026.
- `resultados.json`: temporadas **2024 y 2025 únicamente** (7.722 filas, 429 rondas).

## 2. Tipos de torneo

`calendario.json` trae `tipoTorneo` numérico. El campo `tipoNombre` sólo está
relleno en 2026; para las temporadas anteriores está a `null`, pero la
correspondencia se confirma porque los puntos otorgados siguen la escala del
tipo correspondiente:

| `tipoTorneo` | Nombre |
|---|---|
| 1 | The Final |
| 2 | Normal |
| 3 | Major |

## 3. Escala de puntos individuales

Origen: `TodasDimensiones.xlsx`, hoja **`Nuevos Puntos`**.

| Puesto | Normal | Major | The Final |
|---|---|---|---|
| 1 | 500 | 600 | 1800 |
| 2 | 300 | 330 | 990 |
| 3 | 190 | 210 | 630 |
| 4 | 135 | 150 | 450 |
| 5 | 110 | 120 | 360 |
| 6 | 100 | 110 | 330 |
| 7 | 90 | 100 | 300 |
| 8 | 85 | 94 | 282 |
| 9 | 80 | 88 | 264 |
| 10 | 75 | 82 | 246 |
| 11 | 70 | 77 | 231 |
| 12 | 65 | 72 | 216 |
| 13 | 60 | 68 | 204 |
| 14 | 57 | 64 | 192 |
| 15 | 55 | 61 | 183 |
| 16 | 53 | 59 | 177 |
| 17 | 51 | 57 | 171 |
| 18 | 49 | 55 | 165 |
| 19 | 47 | 53 | 159 |
| 20 | 45 | 51 | 153 |
| 21 | 44 | 50 | 150 |
| 22 | 43 | 49 | 147 |
| 23 | 42 | 48 | 144 |
| 24 | 41 | 47 | 141 |
| 25 | 40 | 46 | 138 |
| 26 | 39 | 45 | 135 |

Los puntos se asignan por `rankingSocios`, **no** por `posicionTorneo`. Las
desviaciones encontradas están listadas en [DIFERENCIAS.md](DIFERENCIAS.md).

## 4. Desempate de posiciones

Criterio, en este orden, **ganando siempre el menor valor**:

1. **Resultado neto** del torneo (suma de las rondas si es a doble vuelta).
2. **Handicap de juego**. En torneos a doble vuelta, la **suma** del handicap de
   juego de todas las rondas.
3. **Últimos 9 hoyos** (10-18) — *ver nota de orden más abajo*.
4. **Últimos 6 hoyos** (13-18).
5. **Últimos 3 hoyos** (16-18).

En torneos a doble vuelta el countback se toma de la **última ronda jugada**.

### Evidencia

Contraste de reglas candidatas contra las 1.097 posiciones de socio registradas
entre 2021 y 2026:

| Regla | Puestos reproducidos |
|---|---|
| neto → hcp de juego → u3 → u6 → u9, menor gana | 1083 / 1097 |
| neto → hcp de juego → u9 → u6 → u3, menor gana | 1079 / 1097 |
| neto → hcp de juego → countback, **mayor** gana | 1047-1051 / 1097 |
| neto → u9 → u6 → u3 (**sin** handicap de juego) | 378 / 1097 |
| neto → bruto | 559 / 577 (2024-2026) |

Conclusiones respaldadas por esos números:

- **El handicap de juego es el segundo criterio, sin duda.** Quitarlo hunde la
  regla de 1.079 a 378 aciertos.
- **Gana el que menos golpes hace** en los segmentos. La variante "mayor gana"
  pierde unos 30 puestos.
- **Da igual usar bruto o neto en el countback.** Se examinaron los 31 grupos de
  empate (mismo neto y mismo handicap de juego) de las seis temporadas y el
  orden resultante es **idéntico** en los 31 con las dos variantes. Es esperable:
  con el mismo handicap de juego en el mismo campo, los golpes de ventaja por
  hoyo son los mismos, así que bruto y neto se diferencian en una constante.

### Nota sobre el orden del countback `[NO VERIFICADO]`

El dato histórico **no es consistente** en el orden de los tres segmentos, y
ningún orden único explica las seis temporadas:

- Con 9 → 6 → 3 quedan **18** puestos sin explicar de 1.097.
- Con 3 → 6 → 9 quedan **14**.
- 3 torneos sólo cuadran con 9 → 6 → 3 y 4 torneos sólo cuadran con 3 → 6 → 9.
- 3 torneos no cuadran con ninguno de los dos.

El desglose torneo a torneo está en
[DIFERENCIAS.md](DIFERENCIAS.md#5-desempates-que-no-cuadran-con-ningún-orden-único--inconsistencia).

La decisión adoptada es **9 → 6 → 3**, que es el countback estándar de golf, y
está registrada en [DECISIONES.md](DECISIONES.md). **No se ha confirmado contra
el reglamento escrito de la liga**, que es la única fuente que zanjaría la
cuestión: el dato, por sí solo, no puede hacerlo.

### El modelo actual no puede reproducir el desempate

Ninguna columna de `clasificacion_YYYY.json` permite recalcular la posición:

- Los segmentos de 9, 6 y 3 hoyos no existen como campo. Hay que calcularlos
  desde el objeto `hoyos` de `tarjetas_YYYY.json`.
- En torneos a doble vuelta, `handicapJuego` guarda **sólo el de la última
  ronda**. Ejemplo comprobado: Alvaro Nieto en el T7 de 2026 tiene
  `handicapJuego: 12`, cuando el desempate usa 29 (17 en Desert Springs + 12 en
  Aguilón).

## 5. Clasificación general de la temporada (`clas_matrix`)

Estructura por jugador: `torneos` (puntos por torneo), `computan` (los torneos
que suman), `nPunt`, `nJugados`, `total`, `rk`.

Invariantes verificados en las seis temporadas, sin una sola excepción:

- `total` == suma de los puntos de los torneos listados en `computan`.
- `computan` == los `nPunt` torneos de mayor puntuación del jugador.
- `nPunt` == `min(nTornPunt del último torneo jugado de la temporada, nJugados)`.
  Verificado en 38 de 38 jugadores de 2026. `nTornPunt` sólo está relleno en el
  calendario de 2026, así que en temporadas anteriores no es evaluable.

En 2026, el último torneo jugado es el T7, con `nTornPunt: 5`: cuentan las 5
mejores puntuaciones de cada jugador.

## 6. Clasificación por equipos

`equipos_clasificacion_YYYY.json` tiene dos bloques: `equipos` (temporada) y
`clasificacion` (una fila por equipo y torneo).

### Puntuación de un equipo en un torneo

**`teamScore` = suma, para cada ronda del torneo, de los 2 mejores `difNeto`
del equipo en esa ronda.** Menor es mejor.

Verificado en las **46 filas** de 2026 que tienen jugadores, sin excepción.
Ejemplo: en el T7, LOS GUARDIANES DEL DATÁFONO obtienen 5 = (−3 + 0 en Desert
Springs) + (4 + 4 en Aguilón), con 5 jugadores en el equipo.

`computa` marca al jugador que entró entre los 2 mejores de alguna ronda. El
flag difiere del cálculo en 3 filas de 2026, y en las tres hay **empate a
`difNeto`** justo en el corte, así que es una elección arbitraria entre iguales
que no altera el `teamScore`.

### Puntos de equipo

`puntosTotales` = `puntosEquipos` + `puntosAsistencia`. Verificado en las 228
filas de 2024, 2025 y 2026 sin excepción.

`puntosEquipos` por `ranking`, de `TodasDimensiones.xlsx` hoja
**`Puntos Equipos`**: 1.º 500, 2.º 400, 3.º 300, 4.º 200, 5.º 175, 6.º 150,
7.º 125, 8.º 100, 9.º 75. Verificado en las 228 filas.

`puntosAsistencia` **no sigue una fórmula única**. Ver
[DIFERENCIAS.md](DIFERENCIAS.md#3-tres-fórmulas-distintas-de-puntos-de-asistencia).

### Equipos sin jugadores suficientes

`valid: false` en las 4 filas de 2026 con 1 o 0 jugadores. Coherente con que el
score necesite 2 jugadores. Esos equipos **siguen recibiendo puntos**: GIMBROS,
con 0 jugadores en el T7, figura 7.º y cobra los 125 puntos del último puesto.

## 7. Invitados

- `jugadores.json` marca la condición por temporada en `tipoParticipacion`:
  `"Si"` (socio), `"Inv"` (invitado), `"No"` (no participa).
- En `tarjetas_YYYY.json` el campo booleano `invitado` **sólo existe en 2026**.
  En temporadas anteriores un invitado se reconoce porque su tarjeta tiene
  `rk: null` y `pts: null`.
- Los invitados **no entran en `clasificacion_YYYY.json`**. La única excepción
  en todo el repositorio es Javier Aguirre en 2026 T3, con la forma que debería
  usarse si se incluyen: `tipoParticipacion: "Inv"`, `rankingSocios: 0`,
  `puntos: 0` y `posicionTorneo` en la escala general.
- Los invitados **sí ocupan puesto en la clasificación general del torneo**
  (`rk` de la tarjeta), que se numera sobre el campo completo, mientras el `rk`
  de un socio se numera **sólo entre socios**. Por eso en el T7 de 2026 hay
  valores de `rk` repetidos: pertenecen a dos escalas distintas.
