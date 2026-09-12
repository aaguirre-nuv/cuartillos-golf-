# Desempates del circuito interno

Escrito el **2026-09-12**. Hasta entonces la regla no estaba en ninguna parte del repo y se había
supuesto dos veces mal.

## La regla

Criterio **RFEG (Libro Verde)** para prueba hándicap Stroke Play, tal como estaban configurados los
torneos en la plataforma de resultados. **Gana siempre el menor número de golpes:**

1. **Resultado neto** del torneo. Si es a doble vuelta, la suma de las rondas.
2. **Hándicap de juego más bajo.** El de juego, **no** el exacto.
3. **Match of cards**: golpes **netos** en los últimos **9, 12, 15, 16 y 17** hoyos, en ese orden.
4. Si el empate persiste, **sorteo**.

Dos precisiones que importan en la práctica:

- **Los «últimos hoyos» son los últimos del campo**, no los últimos que jugó cada participante. Con
  salida a tiro el cálculo no cambia: últimos 9 = hoyos 10 a 18, últimos 12 = hoyos 7 a 18, últimos
  15 = hoyos 4 a 18, últimos 16 = hoyos 3 a 18, últimos 17 = hoyos 2 a 18.
- En torneos **a doble vuelta**, el hándicap de juego es la **suma** de las rondas y el match of cards
  se toma de la **última ronda jugada**.

**Fuente:** [`fuentes/2026-T6-layos-resolucion-desempate.pdf`](fuentes/2026-T6-layos-resolucion-desempate.pdf),
resolución del desempate del torneo 6 de 2026 (Layos, 27/06/2026).

## De dónde salió, y los dos errores previos

El criterio se dedujo primero del dato, y se dedujo **mal, dos veces**:

- Primero se supuso **últimos 9, 6 y 3 hoyos**.
- Luego, **últimos 3, 6 y 9**.

Ninguno de los dos es el correcto: los tramos del reglamento **crecen** (9, 12, 15, 16, 17) y los de
6 y 3 hoyos no existen. La consecuencia fue que **el torneo 6 de 2026 figuró como el error más grave
del repositorio**, con 500 puntos contra 300 entre dos jugadores empatados y ninguna regla que lo
explicara. El dato estaba bien; la regla supuesta estaba mal.

Es la razón de que este documento se escriba con la resolución oficial delante y no con el dato.

### El caso de Layos, comprobado hoyo a hoyo

Luis Fernández y David Sequera empataron a **+1 neto**, los dos con **hándicap de juego 14** (exactos
13,0 y 13,1, que no intervienen). Los datos del repo reproducen el cálculo del documento:

| Tramo | Luis | David | |
|---|---|---|---|
| Hoyos 10-18 (últimos 9) | 0 | 0 | empate |
| Hoyos 7-18 (últimos 12) | **+3** | **−1** | gana David |

De ahí que David Sequera sea el ganador del torneo 6.

## Contraste con el histórico

Aplicando la regla a las **1.097** posiciones de socio registradas entre 2021 y 2026 —dejando fuera
el torneo 7 de 2026, donde los puestos se comparten por la incorporación de Marcos y Nicolás y por
tanto no son comparables—, se reproducen **1.083**.

Comprobaciones que sostienen cada pieza de la regla:

| Variante probada | Puestos reproducidos |
|---|---|
| **La regla: neto → hcp de juego → 9, 12, 15, 16, 17, menos gana** | **1083** |
| Con el match of cards al revés (más golpes gana) | ~1050 |
| **Sin** el hándicap de juego | 378 |
| Sólo neto y bruto | 559 de 577 (2024-2026) |

- **El hándicap de juego es imprescindible**: quitarlo hunde la regla de 1.083 a 378 aciertos.
- **Bruto o neto en el match of cards da lo mismo en la práctica.** Se examinaron los 31 grupos de
  empate de las seis temporadas y el orden resultante es idéntico con las dos variantes: con el mismo
  hándicap de juego en el mismo campo, los golpes de ventaja por hoyo son los mismos, así que bruto y
  neto se diferencian en una constante. El reglamento dice neto, y es lo que se usa.

### Las siete parejas que no cuadran

Quedan **14 puestos** sin explicar, que son **siete parejas de jugadores adyacentes intercambiados**:

| Torneo | Delante según el reglamento | Delante en el dato | Puntos | Criterio que los separa |
|---|---|---|---|---|
| 2022 T2 Naturávila | José Pablo Guil | Nacho González | 80 / 85 | últimos 9: 35 contra 42 |
| 2022 T9 La Faisanera | Angel Hernández | Alvaro Aguirre | 100 / 110 | últimos 12: 49 contra 50 |
| 2022 T9 La Faisanera | Ignacio Cadarso | Alvaro Montoya | 85 / 90 | últimos 9: 40 contra 41 |
| 2023 T7 Valdecañas | Alfonso Hidalgo | Enrique González R | 88 / 94 | últimos 9: 35 contra 37 |
| 2023 T11 Santander | José Pablo Guil | Ignacio Cadarso | 231 / 246 | últimos 9: 40 contra 41 |
| 2024 T11 Santander | Antonio Carmona | Javier González | 0 / 0 | últimos 9: 44 contra 47 |
| **2026 T1 Santander** | **Angel Santana** | **Enrique González R** | 43 / 44 | **hándicap de juego: 2 contra 14** |

El de 2026 T1 es el más claro de todos: no hay tramos que discutir, el reglamento dice que gana el
hándicap de juego más bajo y Angel Santana juega de 2 contra 14.

**Lo que no se puede concluir:** cada caso es una pareja de dos. En un grupo de dos, invertir el orden
es la única alternativa posible, así que decir que «se explican aplicando el criterio al revés» es una
afirmación vacía: no distingue entre criterio invertido, desempate resuelto a mano o sorteo. Son siete
casos aislados en cinco temporadas, todos inversiones de dos puestos adyacentes, y en todos el
criterio que debería separarlos es inequívoco. Nada más se puede afirmar desde aquí.

Una hipótesis compatible con el propio documento del torneo 6, que dice que el torneo «**estaba
configurado** con criterio de desempate RFEG»: el criterio es un ajuste **por torneo** en la
plataforma, y torneos configurados de otra forma explicarían casos aislados. Habría que ver la
configuración de esos seis torneos para saberlo.

## El modelo no guarda con qué desempatar

Ninguna columna de `clasificacion_<año>.json` permite recalcular una posición:

- Los tramos de 9, 12, 15, 16 y 17 hoyos **no existen como campo**. Hay que calcularlos desde el
  objeto `hoyos` de `tarjetas_<año>.json`. Por eso es imprescindible que ese objeto llegue completo.
- En torneos a doble vuelta, `handicapJuego` guarda **sólo el de la última ronda**. Ejemplo: Alvaro
  Nieto en el torneo 7 de 2026 figura con `handicapJuego: 12`, cuando el desempate usa 29 (17 en
  Desert Springs más 12 en Aguilón).

Mientras siga así, **cuando un empate llegue al match of cards conviene dejar el cálculo escrito**,
como se hizo con la resolución de Layos. Es lo que zanja las dudas después.
