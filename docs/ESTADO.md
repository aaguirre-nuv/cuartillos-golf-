# Estado del proyecto

**Al 2026-09-12.** Los estados anteriores están en el historial de git.

---

## Lo primero al volver

Nada urgente del circuito interno: **el torneo 8 ya está cargado**. Lo siguiente es de la liga
federativa: **la inscripción para el 27 de septiembre en Cabanillas abre el lunes 2026-09-14 a las
10:00** y cierra el lunes 21 a la misma hora, por la web de la RFGM, 48 €. Hay un mensaje de WhatsApp
redactado para animar a apuntarse.

## Qué se hizo el 2026-09-12

### Torneo 8 · La Faisanera · Major · par 71

Cargado entero desde los tres Excel del torneo (`Jugadores`, `HANDICAP` y `SCRATCH`). 21 inscritos y
20 con tarjeta: **José Antonio Santana fue baja de última hora** y **Gimbros no presentó a nadie**.

**Gana Miche López con 69 netos.** Marcos Ruiz empata a 69 y es segundo: el desempate lo resuelve el
hándicap de juego, 18 contra 25.

- El **par del campo es 71**, no los 72 que decía el calendario. Lo confirman los Excel (el par sale
  idéntico para los 20 jugadores) y las cinco ediciones anteriores de La Faisanera. Corregido.
- **Las posiciones del Excel coinciden con el criterio RFEG en los 20 jugadores.** Hubo siete empates
  y los siete se resolvieron por hándicap de juego, sin llegar al match of cards.
- Al ser el **sexto torneo puntuable**, la general pasa a contar las **6 mejores** de cada jugador y
  se recalculó entera. Miche López sube del 10º al 2º con los 600 puntos del Major.
- Alta de **Nacho González** en la general: era su primer torneo de 2026.

### Marcos y Nicolás, a Cerdos Arqueros · cerrado el pendiente nº 1

Álvaro confirmó el equipo de los dos. Con ellos, Cerdos Arqueros pasa de **+27 a +17** en el torneo 7,
aunque mantiene el cuarto puesto y sus 200 puntos. En el torneo 8 son 5 jugadores y quedan terceros.

Sus puntos individuales del torneo 7 (90 y 55) **no se han tocado**: estaban bien desde el día 10.

### Puntos de asistencia unificados a 10 por jugador

Había **tres fórmulas distintas** conviviendo en 2026, y ninguna era la de 2025 ni la de la hoja
`Puntos Equipos` del Excel. Por decisión de Álvaro, el criterio es fijo —10 por jugador presentado, sin
excepción por tipo de torneo— y se ha unificado toda la temporada. Afectó a **45 filas** y cambió la
clasificación de equipos. El detalle está en
[`clasificacion-por-equipos.md`](clasificacion-por-equipos.md).

### Documentación

Dos documentos nuevos, con las reglas que estaban en el código y en el dato pero no escritas:

- [`desempates.md`](desempates.md) — el criterio **RFEG (Libro Verde)**: neto, hándicap de juego, y
  match of cards sobre los últimos **9, 12, 15, 16 y 17** hoyos. Con la resolución oficial del torneo
  6 en `fuentes/` como fuente.
- [`clasificacion-por-equipos.md`](clasificacion-por-equipos.md) — cómo se puntúa un equipo, los
  puntos de asistencia y el desempate entre equipos.

**El criterio de desempate se había supuesto mal dos veces** (últimos 9-6-3, y luego 3-6-9). Los
tramos del reglamento crecen, y los de 6 y 3 hoyos no existen. Por esa suposición, el torneo 6 de
Layos llegó a figurar como el error más grave del repositorio cuando el dato era correcto. Está
contado en `desempates.md` para que no se repita.

## Estado actual, frente por frente

### Circuito interno · general

Cuentan las 6 mejores de 8 torneos jugados. Quedan el 9 (Naturávila, 18/10), el 10 (Layos, 28/11) y
la Final (Santander, 19/12).

| | Jugador | Total |
|---|---|---|
| 1 | José Pablo Guil | 1363 |
| 2 | Miche Lopez | 1130 |
| 3 | Alvaro Nieto | 953 |
| 4 | Alvaro Aguirre | 911 |
| 5 | Eduardo Buendía | 895 |

### Circuito interno · equipos

| | Equipo | Total |
|---|---|---|
| 1 | Me Alivio Golf Club | 2540 |
| 2 | La Orden del Swing Sagrado | 2305 |
| 3 | Cerdos Arqueros | 2120 |
| 4 | Los Guardianes del Datáfono | 2115 |
| 5 | No Te La Lleves Mamado | 1855 |
| 6 | La Amenaza Fantasma | 1805 |
| 7 | Gimbros | 1445 |

### CSC · entre semana · Grupo 3

Foro 2000 2 puntos, Club El Estudiante 1, Cuartillos 1, Grow Golf 0. **Club El Estudiante va por
delante pese a peores ups porque el desempate es el enfrentamiento directo**, cuya ida perdimos 1-2.

**La segunda plaza de cuartos se decide entera el 2026-10-01 en El Fresnillo, contra ellos**: hacen
falta 4 de los 6 individuales, o 3,5 ganando la vuelta por 3 ups o más.

### CSC · fin de semana · Grupo 5

Foro 2000 1 punto, Cuartillos 1, Approach y Putt 0, Putt & Drive 0. Quedan dos enfrentamientos, los
dos **con la ida ganada 2-1**: el 2026-09-27 en Cabanillas contra Putt & Drive y el 2026-10-04 en La
Faisanera contra Foro 2000. **Con 2,5 de 5 en cada uno se termina primero de grupo con 3 puntos y se
entra en cuartos sin depender de nadie.** Aquí ser segundo no clasifica solo: hay que estar entre los
tres mejores segundos de cinco grupos, y eso se decide por ups.

## Pendiente

### 1. Regenerar `jugadores.json` para 2026 · lo más importante

`jugadores.json` se dejó de generar en 2025 y **no tiene ni una fila de 2026**. El microsite tira de
ahí para las plantillas, así que desde los datos publicados sólo se puede reconstruir **quién ha
jugado**, que no es lo mismo que **quién está fichado**. La tabla de miembros sí existe y está al
día, en la hoja «Jugadores por EquipoAño» de `datos/TodasDimensiones.xlsx`: son **43 filas de 2026**,
40 con equipo y 3 sin él.

**Marcos Ruiz y Nicolas Sequera ya están en el Excel**, dados de alta el 2026-09-12 en las dos hojas:
`Jugadores` (tabla `dJugador`, filas 58 y 59, con `Si` en 2026 y `No` en las temporadas anteriores) y
`Jugadores por EquipoAño` (tabla `dJugadorEquipo`, filas 115 y 116, en Cerdos Arqueros). Ya no hay
riesgo de que una regeneración se lleve su alta por delante.

Dos cosas de esas altas que conviene repasar: **el mote de Nicolás quedó como «Nico»** y **Marcos se
quedó sin email**, porque el que traía el Excel del torneo era el de David Sequera.

Plantillas actuales (fichados, no jugadores de un torneo):

| Equipo | Fichados |
|---|---|
| Gimbros | 7 |
| No Te La Lleves Mamado | 6 |
| **Cerdos Arqueros** | **7** |
| La Orden del Swing Sagrado | 5 |
| Los Guardianes del Datáfono | 5 |
| Me Alivio Golf Club | 5 |
| La Amenaza Fantasma | 5 |

Más tres socios sin equipo: Franck Benouniche, Jaime de la Cal y Juan Sanz. **Juan Sanz sale en gris
con la etiqueta «sin equipo» y eso es correcto**, decisión de Álvaro del 2026-09-11: «Juan Sanz viene
así». No es un fallo pendiente.

### 2. Dudas abiertas, sin urgencia

- **Siete parejas de desempate que no cuadran** con el criterio RFEG, repartidas en cinco temporadas.
  La más clara es 2026 T1, donde el reglamento daría el puesto a Angel Santana por hándicap de juego
  (2 contra 14) y el dato da el contrario. Detalle y lo que **no** se puede concluir de ellas, en
  [`desempates.md`](desempates.md).
- **Dos ajustes de puntos de 2024 sin explicar**, con el mismo mecanismo de la incorporación pero
  sobre socios antiguos: Ruslan Kochman en Cabanillas y Carlos Maestro en Palomarejos. Detalle en
  [`incorporacion-de-socios.md`](incorporacion-de-socios.md).
- **En el torneo 3 de 2024**, entre tres empatados a `difNeto` 5, el 3º cobra 135 y el 4º cobra 190:
  los puntos cruzados respecto al puesto. Las posiciones sí son correctas según el criterio.
- **El campo `valid` de equipos es inconsistente** con equipos de un solo jugador: en 2026 hay dos
  marcados `false` y uno `true`. Con dos o más nunca ha habido duda.
- **El PDF federativo de fin de semana se contradice en una celda** (Foro 2000 – Putt & Drive: da ida
  12-0 y vuelta 5-1 en ups pero totaliza 17-2). No afecta a Cuartillos.

## Cuatro trampas de este repo

1. **Cambiar un dato no basta: hay que subir `CV` en `microsite.html`.** Si no, los navegadores que ya
   han visitado la página siguen sirviendo la copia vieja, y el dato parece mal cuando está bien.
2. **Un dato correcto puede no verse.** El campo `sinEquipo` a `true` oculta puesto, puntos, total y
   golpes de ventaja de esa fila entera.
3. **El Excel es la fuente; los JSON son la salida.** Corregir solo el JSON deja el origen mal, y la
   próxima regeneración se lleva la corrección por delante.
4. **Comprobar el remoto antes de afirmar nada sobre el estado del dato.** El 2026-09-12 se trabajó
   un rato sobre un clon de nueve días atrás y se llegó a sostener, con evidencia y todo, que Marcos
   y Nicolás no tenían puntos del torneo 7. Los tenían desde el día 10.
