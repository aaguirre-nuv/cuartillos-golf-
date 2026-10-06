# Estado del proyecto

**Al 2026-10-06.** Los estados anteriores están en el historial de git.

---

## Lo primero al volver

**Cuartillos está en cuartos de final en las dos ligas, y las dos fases de grupos están cerradas.**

| Liga | Cómo entró | Cuartos | Rival |
|---|---|---|---|
| Entre semana | 2º del Grupo 3, 2 puntos | **martes 20/10, El Encín** | 1º del Grupo 2, sin decidir |
| Fin de semana | **tercer mejor segundo**, 2 puntos | **domingo 15/11, Los Ángeles de San Rafael** | 1º del Grupo 1, sin decidir |

**Las dos inscripciones están abiertas en el microsite.** Campo neutral las dos, **2 fourball + 2
individuales, 6 jugadores** —no es el formato de la liga—. Plazos federativos: **cierra el miércoles
14/10 a las 10:00** la de entre semana y el **lunes 09/11 a las 10:00** la de fin de semana.

**Lo de fin de semana salió por los pelos.** Se perdió 1-4 en La Faisanera, el grupo se quedó en
segundo, y en esta liga ser segundo no clasifica solo. La RFGM desempató a los tres segundos de 2
puntos por partidos ganados: **AEPJG 16, Cuartillos 13,5 y Colmenar Viejo 13**, así que Colmenar se
queda fuera por medio punto. Detalle en [`reglamento-csc-2026.md`](reglamento-csc-2026.md) §14.3.

**Único dato de liga sin cargar:** Approach y Putt – Putt & Drive de la jornada 6 de fin de semana.
No cambia nada: los dos acabaron con 0 puntos y ninguno podía pasar de 1.

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

### `jugadores.json` regenerado para 2026

Tenía datos hasta 2025 y **ninguna fila de 2026**. Añadidas las **58 filas** de la temporada desde el
Excel: 43 socios, 11 invitados y 4 que no participan, con su equipo, su mote y su liga CSC. Las 324
filas anteriores quedan intactas.

La liga CSC no sale del Excel, que sólo llega a 2025: sale de los elegibles de `datos/csc.json`, 13
de entre semana (`LABOR`) y 26 de fin de semana (`FINDE`), sin ningún jugador en las dos listas.

**Ojo con una idea equivocada que arrastraba este documento**: el microsite **no lee
`jugadores.json`**. No aparece en ninguna de sus llamadas de carga, ni usa `mote`, `icono` ni
`nombreEquipo`. Los ficheros que sí lee son `calendario.json`, `csc.json`, `estadisticas.json`,
`tarjetas_<año>.json`, `clasificacion_<año>.json`, `clas_matrix_<año>.json` y
`equipos_clasificacion_<año>.json`. Así que tener el maestro al día es lo correcto y sirve para
cualquier regeneración, pero **no cambia nada de lo que se ve en la web**.

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

## Qué se hizo el 2026-09-19

### El ranking de selección CSC contaba dos veces los torneos a doble vuelta

El microsite muestra un «Ranking de selección — 2 mejores de últimos 3 torneos liga» por modalidad,
que es criterio del club para elegir a quién llevar, no norma de la RFGM. Tomaba **tarjetas** en vez
de torneos, así que el torneo 7 —a doble vuelta— contaba como dos, y la tabla, que tiene una columna
por torneo, pintaba sólo una de las dos rondas: **el total no cuadraba con lo que se leía**.

Lo destapó **José Antonio Santana**, que mostraba `+12 | +0 | —` con un total de `+4`. Parecía que el
torneo 8, que no jugó, valía 0. No era eso: el `+4` era su segunda ronda del torneo 7, en Aguilón,
que entraba en la cuenta pero no se veía. **Los torneos no jugados no computan, se excluyen.**

Corregido: **un torneo, un resultado**, y en los de doble vuelta la **media de las rondas**, por
decisión de Álvaro. Detalle en [`reglamento-csc-2026.md`](reglamento-csc-2026.md) §15. Cambia el
orden de las dos listas: en fin de semana Luis Fernández pasa a primero y Alvaro Nieto a segundo.

Sólo toca `microsite.html`; no cambia ningún dato.

## Qué se hizo el 2026-09-20

### Beatriz Álvarez y Lucas Arcos, de alta como invitados

Jugaron el torneo 7 y no estaban en el maestro. Añadidos a la hoja `Jugadores` (tabla `dJugador`,
filas 60 y 61) con `Inv` en 2026 y `No` en las temporadas anteriores, y regeneradas las filas de 2026
de `jugadores.json`, que pasa de 58 a 60. **No entran en `Jugadores por EquipoAño`**: esa hoja lleva
sólo socios con equipo.

De ellos **sólo consta nombre y licencia**, sacados de sus tarjetas del torneo 7: Beatriz
`CM00065996` y Lucas `CMA8069482`. **Móvil, email e icono se han dejado vacíos a propósito**, y el
nombre completo repite el corto porque no hay otro dato. Los motes quedaron «Bea» y «Lucas».
Completarlo cuando se sepa.

Con esto **el maestro conoce ya a todos los que tienen tarjeta en 2026**.

## Qué se hizo el 2026-09-23

### Abierta la inscripción del 4 de octubre, con el 27 ya convocado

El microsite sólo permitía **una inscripción abierta por modalidad**, la del primer partido sin
resultado. Con el 27 de septiembre ya convocado pero sin jugar, no había forma de abrir la del 4 de
octubre sin inventarle un resultado al 27.

Un partido de `csc.json` admite ahora **`"inscripcionCerrada": true`**: deja de ser el abierto, pero
se sigue viendo en una tarjeta de sólo lectura con sus convocados y sus parejas, y en el calendario
figura como **CONVOCADO**. Cuando llegue el resultado del 27, esa tarjeta desaparece sola.

Marcado así el **FS5** (27/09, Cabanillas, Putt & Drive), con lo que **FS6** (04/10, La Faisanera,
Foro 2000) pasa a ser el abierto. Entre semana no cambia nada: sigue abierto el ES6 del 1 de octubre.

**La portada también.** Es donde se pulsa para apuntarse, así que en «Próximos eventos» salen las
dos: el 27 con la etiqueta CONVOCATORIA CERRADA y sus convocados, y el 4 con el botón de apuntarse.
Las dos vistas comparten ahora la función `cscPendientes()`; antes la portada tenía su propio bucle,
que no miraba ni los resultados metidos desde el panel ni la marca de cerrada.

Cómo repetirlo cada jornada, y los plazos federativos, en
[`reglamento-csc-2026.md`](reglamento-csc-2026.md) §16.

## Qué se hizo el 2026-10-06

### Cargado el FS6 y cerrada la fase de grupos de fin de semana

**Foro 2000 4 – Cuartillos 1**, en La Faisanera, 12 ups a 5. Gana sólo **Francisco Álvarez, 5&3**;
se pierden los otros cuatro (3&2, 1UP, 6&5 y 2UP). Con la ida ganada 2-1, el enfrentamiento cae
**5-3** y Foro 2000 se lleva el grupo con 3 puntos.

**Cuartillos entra igualmente en cuartos, como tercer mejor segundo.** La RFGM lo resolvió por correo
el mismo día: tres segundos empatados a 2 puntos y desempate por **partidos ganados en los tres
enfrentamientos**, que es el primer criterio de la normativa. **AEPJG 16 · Cuartillos 13,5 · Colmenar
Viejo 13.**

**Los 13,5 de la federación cuadran al decimal con `datos/csc.json`.** No es un detalle: valida las
seis jornadas del grupo, las tres correcciones de §13.2 del reglamento y la forma de contar los
medios puntos. Es el mejor contraste que ha tenido el dato de fin de semana.

**El acta trae los nombres completos y el repo usa los motes.** En el acta figura **Vicente López
Calderón**, que no está en la lista de elegibles y se cargó así, en crudo, en lugar de adivinar. Lo
confirmó Álvaro el 2026-10-06: **es Miche**, y de hecho lo decía ya `jugadores.json`, donde
`Miche Lopez` lleva `nombreCompleto: "Vicente Lopez Calderón"` y licencia `CMA8937096`. Corregido a
**Miche Lopez**, que es como se le nombra en todo el repo.

**La regla que sale de aquí:** las actas federativas vienen con el nombre legal completo y el repo
usa el nombre corto. Antes de dar por bueno que alguien no está en elegibles, **cruzar el nombre del
acta contra `nombreCompleto` de `jugadores.json`**. Hecho con los cinco del FS6, y los cinco cuadran:

| En el acta | En el repo |
|---|---|
| Jose Pablo Guil Salvador | José Pablo Guil |
| Francisco Alvarez Oliva | Francisco Alvarez |
| **Vicente Lopez Calderón** | **Miche Lopez** |
| Jorge Alberto Martinez Sanchez | Jorge Alberto Martínez Sánchez |
| Francisco Javier Gonzalez Salvador | Javier Gonzalez Salvador |

### Abierta la inscripción de los cuartos de fin de semana

**Domingo 15 de noviembre, Los Ángeles de San Rafael**, contra el 1º del Grupo 1. Añadido como
`FSQF` con las mismas tres particularidades que el `ESQF` del 20 de octubre —formato mixto de 6,
campo neutral e id fuera de la serie—, que ya estaban soportadas, así que esta vez **no hubo que
tocar el HTML**. Comprobado ejecutando el microsite.

### Corregido un motivo mal dado sobre los PDF federativos

Durante la fase se dijo aquí y en el reglamento que la carrera de los mejores segundos «no se puede
calcular porque `datos/csc.json` sólo guarda el Grupo 5». **El motivo estaba mal**: los dos PDF de
`docs/fuentes/` traen **todos los grupos** —los 4 de entre semana y los 5 de fin de semana—, y así
lo decía ya el §13.1 del propio reglamento. Lo que sí era cierto es que esos PDF son del 11 de
septiembre y les faltaban las dos últimas jornadas. **Antes de decir que un dato no está, mirar en
`fuentes/`.**

De ahí salió, por ejemplo, la composición del **Grupo 2 de entre semana**: Golf Sierra Norte,
Sultanes del Swing, Goldfers y CG Colmenar Viejo, con el primer puesto decidiéndose entre **Goldfers
y Colmenar Viejo** el 1 de octubre en El Fresnillo.

## Qué se hizo el 2026-10-04

### Abierta la inscripción de los cuartos de entre semana

**Martes 20 de octubre, El Encín.** Añadido a `datos/csc.json` como `ESQF`, detrás de las seis
jornadas de liga, que ya tienen todas resultado: con eso pasa a ser la inscripción abierta de entre
semana, tanto en la sección CSC como en la portada, con su botón **Apuntarme**.

Tres cosas de este partido no son como las de liga, y están explicadas en
[`reglamento-csc-2026.md`](reglamento-csc-2026.md) §16:

- **`"formato": "2 fourball + 2 individuales"`**, que el microsite lee como **6 necesarios** y como
  2 fourballs y 2 individuales en el modal de asignación.
- **`"local": null`**, porque el campo lo pone la federación. Para esto sí hubo que tocar el HTML:
  el calendario solo sabía pintar LOCAL o VISITA, y un `false` habría dicho VISITA, que es falso.
  Ahora pinta **NEUTRAL** cuando `local` viene a `null`.
- **`"id": "ESQF"`**, fuera de la serie ES1..ES6. Nada interpreta el número del id.

**El rival va como `1º del Grupo 2 (cuartos)`** hasta que se sepa el equipo, que es lo que dice el
cuadro match de la circular. Esa cadena sale tal cual en el calendario, en la portada y en el título
de la tarjeta de inscripción.

**Comprobado ejecutando el microsite**, no leyendo el código: `cscPendientes` da `ESQF` como abierto,
`calcNecesarios` da 6, el calendario pinta la fila con NEUTRAL y la portada saca el botón Apuntarme.
Y la página de fin de semana sigue igual, con el FS6 de hoy como próximo.

**Corregida de paso una fila de §16:** el plazo federativo del 1 de octubre estaba calculado con la
regla de los miércoles por ser «entre semana», pero el partido era **jueves** y el plazo lo fija el
día de la semana, no la liga. Las seis jornadas de entre semana de 2026 se jugaron en jueves.

## Qué se hizo el 2026-10-01

### Cargado el ES6 y Cuartillos se mete en cuartos

**Cuartillos 4 – Club El Estudiante 2**, en El Fresnillo, 8 ups a favor y 5 en contra. Ganan Aguirre
(3&2), Buendía (2&1) y Chiralt (3&2); empatan Carlos Maestro y Montoya; pierde Nacho González (5&4).
Con la ida perdida 1-2, el enfrentamiento cae **5-4** y suma el segundo punto de liga.

El dato salió de tres capturas del acta de nextcaddy. **La suma de los seis individuales cuadra con
la cabecera oficial del acta**, 4-2 y 8-5 ups, que es lo que da confianza en la lectura.

Detalle de la clasificación y por qué ya no depende de nadie, en
[`reglamento-csc-2026.md`](reglamento-csc-2026.md) §14.2.

**Encontrado de paso:** el campo `local` de `partidos` se contradice con `partidos_grupo` en **ES1 y
ES5**, que quedan sin tocar. Las filas de grupo son coherentes entre sí —cada pareja juega una vez de
local y otra de visitante— así que el que está mal es el `local` del partido. Sólo afecta a la
etiqueta LOCAL/VISITA del calendario. El del ES6 sí se corrigió al cargarlo.

### Cargado el FS5, que llevaba cuatro días sin acta

**Cuartillos 4 – Putt & Drive 1**, en Cabanillas el 27 de septiembre, **12 ups a favor y ninguno en
contra**. Ganan Ángel Santana (2&1), Francisco Hidalgo (5&4) y Miche López (5&3), y empatan Ángel
Hernández y Santi Díaz: no se perdió ningún partido.

Con la ida ganada 2-1, el enfrentamiento cae **6-2** y suma el segundo punto de liga. Misma
comprobación que en el ES6: **la suma de los cinco individuales cuadra con la cabecera del acta**,
4-1 y 12-0 ups.

Al tener ya resultado, el partido pasa a histórico y se le quitó la marca `inscripcionCerrada`, que
a partir de ahí no pinta nada.

### Cargado también el otro partido de la jornada 5 de fin de semana

**Foro 2000 3,5 – Approach y Putt 1,5**, 10 ups a 1, del acta de nextcaddy «9. FORO 2000 VS APPROACH
Y PUTT». Foro gana tres individuales (4&3, 2&1, 4&3), empata uno y pierde el primero por 1UP. Misma
comprobación de siempre: **3 + 0,5 contra 1 + 0,5 y los ups 4+2+4 contra 1 cuadran con la cabecera**.

No es un partido nuestro, pero **cambia la foto del grupo**: con la ida ya ganada 2-1, Foro cierra el
enfrentamiento en 5,5-2,5 y **sube a 2 puntos, los mismos que Cuartillos**. El domingo deja de ser
«ganar para no depender de nadie» y pasa a ser una final por la primera plaza.

**Encontrado de paso, sin tocar:** la fila de la jornada 5 tiene a **Approach y Putt como local, igual
que la de la jornada 2**, así que ese enfrentamiento figura con el mismo local en la ida y en la
vuelta. El título del acta dice que el 27 de septiembre el local era Foro 2000, o sea que la de la
jornada 5 es la que está del revés. Sólo afecta a la etiqueta del calendario: los puntos y los ups
se han escrito con el equipo correcto. Es el mismo tipo de fallo que el `local` de ES1 y ES5.

### Cargado Grow Golf – Foro 2000 y el Grupo 3 queda cerrado

**Foro 2000 5 – Grow Golf 1**, 19 ups a 5, del acta «5. GROW GOLF VS FORO 2000» del 1 de octubre.
Con la ida ganada 2-1, Foro cierra el enfrentamiento en 7-2 y llega a **3 puntos**.

**Clasificación final del Grupo 3 de entre semana:** Foro 2000 3, **Cuartillos 2**, Club El Estudiante
1, Grow Golf 0. Pasan los dos primeros, así que **Cuartillos va a cuartos como segundo**. Ups de la
liga: 51 a favor y 35 en contra.

**El detalle llegó en dos veces, y eso dejó una pequeña lección.** La primera captura cortaba antes
del sexto individual, así que la fila se cargó con el marcador —seguro, porque lo cierra la cabecera:
Foro con 5 puntos frente a los 4 vistos y 19 ups frente a los 14— pero **sin desglose**, en vez de
rellenar el hueco con un 5&4 o un 5&3 a ojo. Con la captura desplazada apareció: **Mayte Castro Celma
5&3** por Foro 2000, que son exactamente los 5 ups que faltaban. Los seis, en orden del acta: 1UP,
2UP, 6&5 y 5&4 de Foro, **5&4 de Jorge Chamochin** por Grow Golf, y 5&3 de Foro.

La deducción habría acertado el resultado, pero no el margen, y ese es justo el tipo de dato que
luego se cita como si fuera del acta. **Lo que no se ve no se inventa, aunque se pueda adivinar.**

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

### Circuito interno · plantillas de 2026

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

### CSC · entre semana · Grupo 3

**Liga terminada.** Foro 2000 3 puntos, **Cuartillos 2**, Club El Estudiante 1, Grow Golf 0. En el
escenario de 16 equipos pasan los dos primeros de cada grupo, así que **Cuartillos está en cuartos
como segundo de grupo**. Ups de Cuartillos en la liga: **51 a favor, 35 en contra**; los de Foro,
76-28.

**Cuartos: martes 20 de octubre en El Encín**, dato que trajo Álvaro el 4 de octubre. Se juega **en
una sola jornada**, con **6 jugadores: 2 fourball y 2 individuales** —no es el formato de las vueltas
de liga— y en **campo neutral**. El rival es **el 1º del Grupo 2** según el cuadro match
([§8.1](reglamento-csc-2026.md#81-el-cuadro-match-que-en-la-circular-va-como-imagen)), pero **todavía
no se sabe qué equipo es**. La inscripción ya está abierta en el microsite.

**Plazo federativo:** al caer en martes va por la regla de los miércoles, no por la de los lunes que
usaron las seis jornadas de liga (todas en jueves): **abre el miércoles 07/10 a las 10:00 y cierra el
miércoles 14/10 a las 10:00**. Conviene cerrar la convocatoria interna con margen sobre esa fecha.

### CSC · fin de semana · Grupo 5

**Liga terminada.** Foro 2000 3 puntos, **Cuartillos 2**, Approach y Putt 0, Putt & Drive 0. Se
perdió 1-4 la vuelta del 2026-10-04 en La Faisanera y el enfrentamiento con Foro cayó 5-3. Ups de
Cuartillos en la liga: **37 a favor, 25 en contra**; partidos ganados, **13,5**.

**Clasificado como tercer mejor segundo**, por resolución de la RFGM: tres segundos empatados a 2
puntos y desempate por partidos ganados —AEPJG 16, Cuartillos 13,5, Colmenar Viejo 13—. **Cuartos
contra el 1º del Grupo 1, el domingo 15 de noviembre en Los Ángeles de San Rafael.**

**Los 13,5 de la federación cuadran exactamente con lo que tiene el repo.** Es la mejor validación
que ha tenido el dato de fin de semana.

## Pendiente

### 1. Javier Dodero figura como socio en el torneo 2, y es invitado

**El maestro lo confirma**: `dJugador` lo tiene como `Inv` en 2026. Pero el dato publicado dice otra
cosa, y encima dice dos cosas distintas entre sí:

| | |
|---|---|
| `tarjetas_2026.json` | `invitado: false`, `rk: 19`, **`pts: 47`** |
| `clasificacion_2026.json` | `tipoParticipacion: "Si"`, `rankingSocios: 19`, **`puntos: 0`** |

Es la **única incoherencia entre tarjetas y clasificación de las seis temporadas**. Y al ocupar un
puesto de socio, los tres que van por debajo cobraron los puntos de un puesto peor del que les tocaba:
Enrique Gonzalez R 45 en vez de 47, Joaquín Sánchez 44 en vez de 45 y Alvaro Nieto 43 en vez de 44.
A los tres les computa el torneo 2, así que son +2, +1 y +1 en la general.

La forma correcta si se decide dejarlo en la clasificación es la que ya usa Javier Aguirre en el
torneo 3: `tipoParticipacion: "Inv"`, `rankingSocios: 0`, `puntos: 0`.

**Pendiente de decisión**: cambia puntos ya publicados de tres socios.

### 2. Criterio de selección CSC · revisado y aplazado a 2027

Se le dio una vuelta el 2026-09-20 y **se decidió dejarlo como está esta temporada**. Las dos ideas
que se valoraron, con lo que salió al medirlas, y lo de fondo —separar forma de implicación— están en
[`reglamento-csc-2026.md`](reglamento-csc-2026.md) §15. **No volver a discutirlo desde cero: leer eso
primero.**

### 3. Dudas abiertas, sin urgencia

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

### 4. Faltan los dos rivales de cuartos

Fechas y campos ya los tenemos; lo que falta es **quién gana el Grupo 2 de entre semana** y **quién
gana el Grupo 1 de fin de semana**. Mientras tanto los partidos están en `csc.json` como `ESQF` y
`FSQF` con `rival` puesto a `1º del Grupo 2 (cuartos)` y `1º del Grupo 1 (cuartos)`; cuando se sepan,
se cambian esas dos cadenas y se sube `CV`, nada más.

Del Grupo 2 de entre semana sabemos por el PDF federativo que se jugaba entre **Goldfers y CG
Colmenar Viejo** el 1 de octubre. Del Grupo 1 de fin de semana (Golf de Golfos, Tres Cantos, CG
Caminos y Grow Golf) hacían falta las jornadas del 27/09 y el 04/10, que no tenemos.

### 5. Los nombres de `jugadores` de `csc.json` están sin normalizar

Son texto libre y cada partido se cargó a su manera. El **FS4** guarda `Angel Hernandez Rilova`,
`Jaime Villanueva Ghisleri`, `Jorge Alberto Martinez`, `Alvaro Nieto Esteban` y `Santiago Diaz`,
ninguno de los cuales coincide con la lista de elegibles; el **FS2** y el **FS3** usan `Jose Pablo
Guil` y `José Pablo Guil`, con y sin tilde, para la misma persona. Del FS5 en adelante se usan los
nombres de elegibles.

No rompe nada —esos nombres sólo se pintan como texto bajo el resultado del partido— pero impide
cruzarlos con `jugadores.json` sin trabajo. Si alguna vez se quiere contar cuántos CSC ha jugado cada
uno, hay que normalizarlos antes. **No tocado: son dato, y cambiarlos necesita el ok de Álvaro.**

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
