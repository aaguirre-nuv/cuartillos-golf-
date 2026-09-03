# Diferencias e incoherencias detectadas

Resultado de auditar `datos/` contra las reglas documentadas en
[MODELO.md](MODELO.md). Cada punto lleva la evidencia con la que se detectó y el
impacto que tendría corregirlo. **Ninguna de estas diferencias se ha corregido**:
el dato está tal cual estaba.

Clasificación usada:

- **Error** — el dato se contradice a sí mismo o contradice su propia escala.
- **Inconsistencia** — dos partes del histórico aplican criterios distintos, sin
  que se pueda saber cuál es el correcto desde el dato.
- **Hueco del modelo** — falta información para poder aplicar la regla.

---

## 1. Javier Dodero de Solano, 2026 T2 Palomarejos — **Error**

Es la **única incoherencia entre `tarjetas_*` y `clasificacion_*` de todo el
repositorio**: se comprobaron las seis temporadas comparando `pts` y `rk` de la
tarjeta contra `puntos` y `rankingSocios` de la clasificación, y sólo aparece
esta.

| Fichero | Contenido |
|---|---|
| `tarjetas_2026.json` | `invitado: false`, `rk: 19`, **`pts: 47`** |
| `clasificacion_2026.json` | `tipoParticipacion: "Si"`, `rankingSocios: 19`, **`puntos: 0`** |

Los dos ficheros dicen cosas distintas, y los dos lo tratan como socio cuando es
invitado. Al ocupar el puesto 19 del ranking de socios, los tres socios por
debajo cobraron los puntos de un puesto peor del que les correspondía:

| Jugador | Puesto real | T2 actual | T2 según escala | ¿computa entre sus mejores 5? |
|---|---|---|---|---|
| Enrique Gonzalez R | 19.º | 45 | 47 | Sí, +2 al total |
| Joaquín Sánchez | 20.º | 44 | 45 | Sí, +1 al total |
| Alvaro Nieto | 21.º | 43 | 44 | Sí, +1 al total |

Forma correcta si se decide dejarlo en la clasificación: la que ya usa Javier
Aguirre en 2026 T3, que es el único invitado presente en un
`clasificacion_*.json` — `tipoParticipacion: "Inv"`, `rankingSocios: 0`,
`puntos: 0`.

---

## 2. Puntos cruzados del 3.º y 4.º, 2024 T3 Cabanillas — **Error**

| Puesto | Jugador | Puntos otorgados | Escala Normal |
|---|---|---|---|
| 3.º | Angel Santana | 135 | **190** |
| 4.º | Javier Gonzalez Salvador | 190 | **135** |

Los dos empataron a 77 netos. Las **posiciones son correctas** según el criterio
de desempate (la regla reproduce ese torneo sin discrepancias); son los puntos
los que están intercambiados. Angel Santana tiene 55 puntos de menos en 2024 y
Javier González 55 de más.

---

## 3. Tres fórmulas distintas de puntos de asistencia — **Inconsistencia**

`puntosAsistencia` de `equipos_clasificacion_*.json`, por número de jugadores
que el equipo presenta:

| Jugadores | 2024 | 2025 | 2026 T1, T2, T3, T7 | 2026 T4, T5, T6 | Excel `Puntos Equipos` |
|---|---|---|---|---|---|
| 1 | 0 | 10 | 10 | 30 | 10 |
| 2 | 0 | 20 | 30 | 60 | 20 |
| 3 | 0 | 30 | 60 | 90 | 30 |
| 4 | 0 | 40 | 100 | 120 | 40 |
| 5 | — | — | 150 | — | 50 |

Evidencia: 96 filas de 2024 con asistencia 0; 84 filas de 2025 con exactamente
10 × n; en 2026, 32 filas con la serie acumulada (10, 30, 60, 100, 150) y 16
filas con 30 × n.

Las dos fórmulas de 2026 coinciden sólo cuando el equipo presenta 5 jugadores.
La columna del Excel admite las dos lecturas: si su valor es el total para n
jugadores sale 10 × n (lo que se aplicó en 2025), y si es lo que aporta el
jugador n-ésimo sale la serie acumulada (lo que se aplicó en 4 torneos de 2026).
**Ninguna de las dos lecturas produce el 30 × n de T4, T5 y T6.**

Impacto: los puntos de equipo de esos tres torneos están entre 20 y 30 por
encima de lo que darían las otras fórmulas, en todos los equipos a la vez.

---

## 4. Cola de puntos del 2026 T5 Lerma — **Error**

| Puesto | Otorgado | Escala Normal |
|---|---|---|
| 21.º Jesus Touceda | 43 | 44 |
| 22.º Enrique Gonzalez R | 41 | 43 |
| 23.º Javier Gonzalez Salvador | 39 | 42 |
| 24.º Javier Cervera | 38 | 41 |

Del 1.º al 20.º el torneo sigue la escala exactamente. La cola baja de dos en
dos en vez de uno en uno. La escala del Excel (hoja `Puntos Torneo`, que llega
al puesto 36) confirma 44, 43, 42, 41 para esos puestos.

---

## 5. Siete parejas con el desempate al revés — **Inconsistencia**

Aplicando el criterio RFEG documentado en
[MODELO.md](MODELO.md#4-desempate-de-posiciones), **1.083 de los 1.097** puestos
de socio de 2021-2026 se reproducen. Los 14 restantes son **7 parejas de
jugadores adyacentes intercambiados** dentro de un empate:

| Torneo | Delante según el reglamento | Delante en el dato | Puntos | Criterio que los separa |
|---|---|---|---|---|
| 2022 T2 Naturávila | José Pablo Guil | Nacho González | 80 vs 85 | últimos 9: 35 contra 42 |
| 2022 T9 La Faisanera | Angel Hernández | Alvaro Aguirre | 100 vs 110 | últimos 12: 49 contra 50 |
| 2022 T9 La Faisanera | Ignacio Cadarso | Alvaro Montoya | 85 vs 90 | últimos 9: 40 contra 41 |
| 2023 T7 Valdecañas | Alfonso Hidalgo | Enrique González R | 88 vs 94 | últimos 9: 35 contra 37 |
| 2023 T11 Santander | José Pablo Guil | Ignacio Cadarso | 231 vs 246 | últimos 9: 40 contra 41 |
| 2024 T11 Santander | Antonio Carmona | Javier González | 0 vs 0 | últimos 9: 44 contra 47 |
| **2026 T1 Santander** | **Angel Santana** | **Enrique González R** | 43 vs 44 | **hándicap de juego: 2 contra 14** |

En los 7 casos el jugador que el reglamento pone delante figura justo detrás. El
más llamativo es **2026 T1**, donde no es una cuestión de tramos de hoyos: Angel
Santana juega de 2 y Enrique González de 14, y el reglamento es explícito en que
gana el hándicap de juego más bajo.

### Lo que no se puede concluir

Cada discrepancia es una pareja de dos jugadores. En un grupo de dos, invertir el
orden es la **única** alternativa posible, así que "se explican aplicando el
criterio al revés" es una afirmación vacía: no distingue entre un criterio
aplicado invertido, un desempate resuelto a mano, o un sorteo. **`[NO VERIFICADO]`**

Lo que sí se puede afirmar con el dato:

- Son 7 casos aislados en 5 temporadas, no un patrón sistemático. 2021 y 2025 no
  tienen ninguno.
- Todas son inversiones de dos posiciones adyacentes, nunca permutaciones
  mayores.
- En cada una, el criterio que debería separarlos es **inequívoco**, no un
  empate ajustado.

Una hipótesis compatible con el propio documento del T6: la resolución dice que
"el torneo **estaba configurado** con criterio de desempate RFEG", lo que indica
que el criterio es un ajuste **por torneo** en la plataforma que produce los
resultados. Torneos configurados de otra forma explicarían discrepancias
aisladas. Es una hipótesis, no una conclusión: haría falta ver la configuración
de esos 6 torneos. **`[NO VERIFICADO]`**

### Resuelto: 2026 T6 Layos

En una versión anterior de este documento, el T6 de 2026 (Layos) figuraba como la
diferencia de mayor peso: 500 puntos contra 300 entre dos jugadores empatados,
sin regla que lo explicase. **Ya está explicado y el dato es correcto.**

La resolución oficial
([`reglamento/2026-T6-layos-resolucion-desempate.pdf`](reglamento/2026-T6-layos-resolucion-desempate.pdf))
documenta el cálculo: Luis Fernández y David Sequera empataron a +1 neto con
hándicap de juego 14 los dos; en los últimos 9 hoyos ambos sumaron 0, y en los
últimos 12 David sumó −1 frente a +3 de Luis. Los datos del repositorio
reproducen esas cifras exactamente, hoyo por hoyo.

El error estaba en la regla que se había supuesto (últimos 9, 6 y 3), no en el
dato. Es la razón por la que este documento no da por buena ninguna regla que no
tenga una fuente documental detrás.

## 6. La Final de 2024 no otorgó puntos — **Pendiente de confirmar**

2024 T11 Santander, tipo The Final: los 27 socios clasificados tienen
`puntos: 0`, cuando la escala The Final va de 1800 a 153. Las Finales de las
demás temporadas sí siguen la escala (2023 T11 reparte 246, 231 y siguientes).

No se puede saber desde el dato si fue una decisión de aquella temporada o un
cálculo que quedó sin hacer. **`[NO VERIFICADO]`**

---

## 7. `jugadores.json` no tiene la temporada 2026 — **Hueco del modelo**

El maestro de jugadores cubre 2020 a 2025. No existe ninguna fila de 2026, así
que hoy **no hay dónde declarar que un jugador es socio en 2026**, ni su equipo,
ni su `idTempJugador` de la temporada.

En la práctica el estado de socio de 2026 vive en dos sitios derivados:
`invitado` en `tarjetas_2026.json` y `tipoParticipacion` en
`clasificacion_2026.json`. Es de ahí de donde lo lee el microsite.

---

## 8. `handicapJuego` no sirve para desempatar a doble vuelta — **Hueco del modelo**

En `clasificacion_*.json`, un torneo a doble vuelta guarda **una sola fila** por
jugador, y su `handicapJuego` es el de la **última ronda**, no la suma.

Evidencia: Alvaro Nieto en 2026 T7 tiene `handicapJuego: 12`, mientras el
desempate usa 29 (17 en Desert Springs + 12 en Aguilón).

Consecuencia: la posición oficial de un torneo a doble vuelta **no se puede
recalcular** con los campos que hoy existen en la clasificación. Hay que ir a las
tarjetas de las dos rondas.

---

## 9. El campo `invitado` sólo existe en 2026 — **Hueco del modelo**

`tarjetas_2026.json` tiene el booleano `invitado`. Las temporadas 2021-2025 no lo
tienen: allí un invitado sólo se distingue porque su tarjeta lleva `rk: null` y
`pts: null`, que es una convención implícita y no un dato explícito.

---

## 10. `resultados.json` sólo cubre 2024 y 2025 — **Hueco del modelo**

El golpe a golpe existe para 2024 y 2025 (7.722 filas, 429 rondas). Para 2021,
2022, 2023 y 2026 el grano más fino disponible es el objeto `hoyos` de las
tarjetas.

---

## 11. Los `computa` de equipos con empate son arbitrarios — **Cosmético**

En 3 de las 46 filas de equipos de 2026 con jugadores, el conjunto de jugadores
marcados con `computa: true` no coincide con el que sale de aplicar la regla, y
en las tres hay **empate a `difNeto`** justo en el corte de los 2 mejores:

- 2026 T1 LOS GUARDIANES: Carmona y Jorge Martínez empatan a +7.
- 2026 T2 ME ALIVIO: Alfonso Hidalgo y José Pablo Guil empatan a +6.
- 2026 T4 LA ORDEN: Javier Chiralt y Nacho Casas empatan a 0.

El `teamScore` es el mismo en cualquier caso, así que no afecta a la
clasificación. Sólo cambia a quién se le atribuye el mérito.

---

## Lo que sí cuadra

Para dimensionar lo anterior, esto se verificó sin una sola excepción:

- `clas_matrix_*`: `total` == suma de los torneos que computan, y `computan` ==
  los `nPunt` mejores, en las seis temporadas y sus 182 fichas de jugador.
- `nPunt` == `min(nTornPunt del último torneo jugado, nJugados)`, 38 de 38
  jugadores de 2026.
- `teamScore` == suma por ronda de los 2 mejores `difNeto`, 46 de 46 filas de
  2026.
- `puntosTotales` == `puntosEquipos` + `puntosAsistencia`, y `puntosEquipos` ==
  escala por `ranking`, en las 228 filas de 2024, 2025 y 2026.
- Coherencia `pts`/`rk` entre tarjetas y clasificación: 1 sola incoherencia en
  seis temporadas, la del punto 1.
