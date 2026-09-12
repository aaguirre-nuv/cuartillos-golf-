# Clasificación por equipos del circuito interno

Escrito el **2026-09-12**, al cargar el torneo 8. Las reglas estaban en el código y en el dato, pero
no escritas. Cada una lleva con qué se verificó.

Vive en `datos/equipos_clasificacion_<año>.json`, con dos bloques: `equipos` (la temporada) y
`clasificacion` (una fila por equipo y torneo).

## Puntuación de un equipo en un torneo

**`teamScore` = suma, para cada ronda del torneo, de los 2 mejores `difNeto` del equipo en esa ronda.**
Menor es mejor.

Verificado en las **52 filas** de 2026 que tienen jugadores, sin excepción. En torneos a doble vuelta
los dos que cuentan **se eligen ronda a ronda**, así que pueden ser jugadores distintos en cada una:
por eso las filas de esos torneos llevan `computaR1` y `computaR2` además de `computa`.

Ejemplo del torneo 7 de 2026, Cerdos Arqueros con 5 jugadores:

| Ronda | Dos mejores | Suma |
|---|---|---|
| Desert Springs | Javier Arcos +5, Alejandro Arcos +6 | +11 |
| Aguilón | Marcos Ruiz +3, Nicolas Sequera +3 | +6 |
| | **teamScore** | **+17** |

`computa` marca a quien entró entre los 2 mejores de alguna ronda. Cuando hay **empate a `difNeto`**
justo en el corte, cuál de los dos se marca es indiferente: el `teamScore` es el mismo. En 2026 pasa
en tres filas.

## Puntos de equipo

`puntosTotales` = `puntosEquipos` + `puntosAsistencia`.

**`puntosEquipos` por `ranking`**, de la hoja `Puntos Equipos` de `datos/TodasDimensiones.xlsx`:

| Puesto | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Puntos | 500 | 400 | 300 | 200 | 175 | 150 | 125 | 100 | 75 |

**`puntosAsistencia` = 10 por cada jugador que el equipo presenta.** Decisión de Álvaro del
2026-09-12: el criterio es fijo y no cambia por tipo de torneo ni por ningún otro motivo.

Un equipo que no presenta a nadie **sigue recibiendo los puntos del último puesto**: Gimbros, con 0
jugadores en los torneos 7 y 8 de 2026, figura séptimo y cobra 125.

### El lío de la asistencia, y cómo quedó

Antes del 2026-09-12 había **tres fórmulas distintas** conviviendo:

| Jugadores | 2024 | 2025 | 2026 T1, T2, T3, T7 | 2026 T4, T5, T6 | **Desde 2026-09-12** |
|---|---|---|---|---|---|
| 1 | 0 | 10 | 10 | 30 | **10** |
| 2 | 0 | 20 | 30 | 60 | **20** |
| 3 | 0 | 30 | 60 | 90 | **30** |
| 4 | 0 | 40 | 100 | 120 | **40** |
| 5 | — | — | 150 | — | **50** |

En 2024 no se repartían puntos de asistencia. 2025 usó 10 por jugador en sus diez torneos, sin una
excepción. **2026 cambió a mitad de temporada y volvió atrás**, sin que el cambio siga ningún patrón:
no es por tipo de torneo, porque el T4 es Major y usa la misma fórmula que el T5 y el T6, que son
normales, mientras que el T1, T2, T3 y T7 también son normales y usan otra.

El 2026-09-12 se unificó toda la temporada 2026 a **10 por jugador**, que es lo que hizo 2025 entero y
lo que dice la hoja del Excel. Afectó a 45 filas y cambió la clasificación de equipos de la temporada.

## Desempate entre equipos

**El mismo criterio que el individual**: primero el hándicap de juego, luego los hoyos. Decisión de
Álvaro del 2026-09-12, aplicada sobre la **suma del hándicap de juego de los jugadores que puntúan**.

Se estrenó en el torneo 8, con La Orden del Swing Sagrado y La Amenaza Fantasma empatadas a +13: 15
contra 41 de hándicap sumado, así que La Orden queda quinta con 175 y La Amenaza sexta con 150.

## Clasificación de temporada

En el bloque `equipos`, por cada equipo:

- `torneos`: los `puntosTotales` de cada torneo.
- `nPunt` = `min(nTornPunt del último torneo jugado, nJugados)`, igual que en la individual.
- `computan`: los `nPunt` torneos de más puntuación.
- `total`: la suma de esos.

Desde el torneo 8 de 2026, `nTornPunt` es **6**: cuentan los seis mejores torneos de cada equipo.

## El campo `valid`

Marca si la puntuación del equipo es comparable. En el dato **no es consistente**: en 2026 hay equipos
con un solo jugador marcados `valid: false` (torneos 2 y 4) y otro marcado `valid: true` (torneo 6).
Con dos jugadores o más nunca ha habido duda. Queda pendiente de aclarar qué debe hacer con uno solo.
