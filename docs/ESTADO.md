# Estado del proyecto

**Al 2026-10-06.** Los estados anteriores están en el historial de git.

---

## Frente nuevo · evolución de forma y hándicap por jugador (2026-10-20, en exploración)

Álvaro quiere ver en el microsite la evolución semanal de cada socio —forma y hándicap— como ayuda
para seleccionar a la CSC. Se está definiendo; **no hay nada construido ni diseño aprobado**. Las
fuentes de la RFEG medidas el 2026-10-20 están en [`fuentes-rfeg.md`](fuentes-rfeg.md): el hándicap
actual de cualquier licencia sale de una API pública de la web nueva, pero **las vueltas de otros
jugadores no tienen hoy fuente pública** (la página antigua de las 20 últimas está rota).

`docs/Untitled-1.txt` y `docs/Untitled-2.txt` son el texto de los dos flujos antiguos de PAD: **sin
subir a propósito** (pesan 6 MB y llevan el usuario de la web).

**Para retomar (fin de semana del 24-25/10):** Álvaro dice que ha visto y extraído las vueltas de
todos sin problema. Primer paso: que inicie sesión en MIGOLF y ver juntos cómo se llega a las vueltas
de otra licencia. Después, seguir definiendo qué tiene que enseñar el microsite; quedó sin contestar
**qué miró y qué echó en falta la última vez que eligió a quién llevar a un partido de la CSC**.

## Frente abierto · rediseño de la sección CSC (2026-10-26)

**El plan está en [`rediseno-csc.md`](rediseno-csc.md). Leerlo antes de tocar la sección CSC o
`csc.json`.** Decidido con Álvaro: **la convocatoria va arriba**, el alcance es **todo lo que se
pueda traer de nextcaddy** y se hace **ya, sobre la temporada en curso**.

**Lo que bloquea el alcance completo es la red del entorno**, que no deja entrar en
`www.nextcaddy.com` ni en `fedgolfmadrid.com`. Se abre en el menú del entorno → Edit → Network
access. Mientras no esté, se trabaja con nuestro grupo; el modelo está pensado para que ampliar el
alcance sea añadir filas, no cambiar la estructura.

## Lo primero al volver

**Entre semana se acabó: Cuartillos cayó en cuartos el 20 de octubre.** Perdió **1,5-2,5 contra
Goldfers** en El Encín. **Queda viva la de fin de semana**, cuyo cuarto de final es el **domingo 15 de
noviembre en Los Ángeles de San Rafael**, contra el 1º del Grupo 1, que aún no se sabe quién es.

| Liga | Cómo entró | Cuartos | Resultado |
|---|---|---|---|
| Entre semana | 2º del Grupo 3, 2 puntos | martes 20/10, El Encín | **perdido 1,5-2,5 vs Goldfers** |
| Fin de semana | tercer mejor segundo, 2 puntos | **domingo 15/11, Los Ángeles de San Rafael** | pendiente |

**La inscripción de fin de semana está abierta** en el microsite. Campo neutral, **2 fourball + 2
individuales, 6 jugadores** —no es el formato de la liga—. El plazo federativo **cierra el lunes 09/11
a las 10:00**.

**Y el T9 del circuito interno se ha movido dos veces**: del domingo 18 de octubre al sábado 31, y de
ahí al **domingo 22 de noviembre en El Encin**, ya con enlace de inscripción nuevo. Entre el T9 y el
T10 de Layos quedan seis días.

**Datos sin cargar, los dos inocuos:** Approach y Putt – Putt & Drive de la jornada 6 de fin de
semana (los dos acabaron con 0 puntos y ninguno podía pasar de 1), y los otros tres cuartos de final
de cada liga, que no son nuestros.

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

## Qué se hizo el 2026-10-22

### Alta de tres elegibles en fin de semana

**Jaime Villanueva, Marcos Ruiz y Nicolás Sequera**, con su licencia de `jugadores.json`. Jaime ya
había jugado el FS4 del 13 de junio sin estar en la lista; Marcos y Nicolás son los socios que se
incorporaron esta temporada. El criterio, de Álvaro: **el que no esté en entre semana va a fin de
semana**.

La lista pasa de **26 a 29 de los 30** que permite el §3, así que **queda un solo hueco**. También se
ha puesto `ligaCSC` a `FINDE` en sus filas de 2026 de `jugadores.json`, que es el reflejo de estas
listas. Comprobado que ninguno de los tres estaba en la lista de entre semana: el §3 prohíbe estar en
las dos.

**Queda pendiente lo que de verdad les habilita**, que es constar en la lista de la RFGM. Ver el
pendiente nº 6.


### Por qué el microsite no se actualizaba aunque se subiera `CV`

**El busca-caché vivía dentro del fichero que se cachea.** `CV` es una variable de `microsite.html`,
y `load()` la pega a cada JSON. Si el navegador sirve su copia guardada del HTML, usa el **`CV`
viejo**, pide el JSON con esa misma URL y se la da también de su caché. Resultado: subir `CV`,
publicar, y que el usuario siga viendo lo de antes. Es exactamente lo que pasó con el cuarto de final
de entre semana.

**Arreglado con `fetch(..., {cache:'no-cache'})`** en `load()`. Eso obliga al navegador a
**revalidar** contra el servidor en vez de servir a ciegas: si el fichero no ha cambiado, GitHub
Pages responde un 304 vacío y no cuesta nada; si ha cambiado, llega el nuevo. Los JSON que carga la
página son pequeños —`resultados.json`, que pesa 4,5 MB, **no lo pide nadie**— así que el coste es
despreciable.

**Lo que esto no arregla:** el propio `microsite.html`. Un cambio de código o de maquetado sigue
necesitando que el navegador se baje el HTML otra vez. Pero los cambios de **dato**, que son casi
todos, ya no dependen de eso.


### Cargado el cuarto de final de entre semana · eliminados

**Goldfers 2,5 – Cuartillos 1,5**, en El Encín, 7 ups a 3. El acta reparte el cuarto de final en dos
rondas, y así está grabado el `detalle`:

| Ronda | | Resultado |
|---|---|---|
| 1 · individuales | Álvaro Aguirre | **G 3&2** |
| 1 · individuales | Eduardo Buendía | P 5&4 |
| 2 · fourball | Montoya + Chiralt | **A/S** |
| 2 · fourball | Nacho González + Sequera | P 2UP |

Individuales 1-1, fourball 0,5-1,5. **La suma cuadra con la cabecera** en puntos y en ups, que es la
comprobación de siempre.

**Y con eso se fija el rival que estaba sin nombre:** el 1º del Grupo 2 de entre semana es
**Goldfers**, que ganó su vuelta a CG Colmenar Viejo el 1 de octubre.

**Dos cosas de los nombres**, las dos cruzadas contra `nombreCompleto` de `jugadores.json` antes de
cargar nada:

- **Ignacio González Salvador es Nacho González**, el mismo que no se presentó al ES6. Aquí sí
  jugó.
- **Eduardo Buendía no casaba** porque el maestro tenía su `nombreCompleto` con una errata:
  **«Eduado Buendía Pan»**, sin la erre. Se identificó por los apellidos y el mismo día se corrigió
  **en el Excel y en `jugadores.json`**, que son las 7 filas del jugador, una por temporada.

  La errata era una **cadena compartida suelta** de `xl/sharedStrings.xml` y salía una sola vez, así
  que se reescribió el zip entrada por entrada cambiando solo ese `<si>`: ni se añade ni se quita
  ninguna entrada, los índices no se mueven y **de las 144 entradas del libro cambia una**, lo que se
  comprueba en el propio script. **Nunca abrir este libro con openpyxl**: tiene tablas dinámicas,
  modelo de datos y Power Query, y guardarlo con openpyxl se los carga.

**En el microsite**, entre semana se queda sin inscripción abierta —la temporada ha terminado— y el
calendario pinta el cuarto como PERDIDO. De paso desaparece el «¡HOY!» que la portada enseñaba desde
el día 20, que era el partido sin resultado.

## Qué se hizo el 2026-10-18

### El T9 de Naturávila queda aplazado, sin fecha

Primero se movió del domingo 18 al sábado 31, y el 18 se cayó también el 31. **No está cancelado:
está pendiente de recolocar.** En `calendario.json` lleva ahora `"aplazado": true`, la observación
«Aplazado · fecha por determinar» y **sin `urlGolfDirecto`**, porque sin fecha no tiene sentido que
nadie se inscriba.

**La fecha del 31 se ha dejado puesta a propósito**, solo para que el torneo no se descoloque en el
calendario: el microsite ordena por fecha y `parseDate(null)` devuelve el día de hoy, que sería peor.
Lo que manda es el flag.

**Esto sí tocó el HTML**, porque no había forma de representar un torneo aplazado:

- La portada y el calendario **ya no lo toman como «próximo»**. Ahora el próximo evento es el cuarto
  de final del CSC del 20 de octubre, y después el T10 de Layos.
- El calendario le pinta una etiqueta **APLAZADO** en vez de «Pendiente».

### El T10 pasa a ser el 7º puntuable

**Decisión de Álvaro.** Si el T10 de Layos se juega antes que el T9, será el noveno torneo de la
temporada, y tras nueve cuentan las **7 mejores**. Así que el T10 pasa de `nTornPunt` 8 a **7**; el
T11 se queda en 8.

**Si el T9 se recoloca, hay que volver aquí.** La serie de `nTornPunt` está calculada suponiendo que
el T10 se juega antes; si al final el T9 cae en medio, los números de los tres últimos torneos hay
que revisarlos. **No deducirlos del dato**: preguntar.

## Qué se hizo el 2026-10-12

### El 5&4 de Nacho González en el ES6 era una incomparecencia

Estaba convocado, llegó tarde y el partido se dio por perdido. El reglamento salda la ausencia de un
jugador justo con un **5&4** (§6), que es exactamente lo que figuraba en el acta, así que **el dato
parecía un partido jugado y perdido**. Marcado en `csc.json` con
`"incomparecencias": ["Nacho Gonzalez"]` en el ES6.

**El marcador y los ups no cambian** —el 4-2 y el 8-5 son los mismos—; lo que cambia es la lectura
por jugador: esa derrota no es suya en el campo.

**Y hay una consecuencia para más adelante.** Para jugar la **Final** hace falta *haber disputado* al
menos una prueba de la temporada (§3 y §9). Un walkover no es haber disputado nada, así que si el ES6
es su única aparición del año —y lo es, en todo el CSC del repo— **para la Final podría no valerle**.
Para cuartos y semifinales da igual: ahí no hay requisito de participación. Conviene saberlo antes y
no el día de la convocatoria.

### El Fresnillo y Naturávila son el mismo campo

Lo confirmó Álvaro. `csc.json` lo llama **El Fresnillo**, que es como viene en las actas de la RFGM;
`calendario.json` y `campos.json` lo llaman **Naturávila**, que es como lo llamamos nosotros. Por eso
buscar «Naturávila» en el CSC no daba nada.

No se ha unificado: cada fichero usa el nombre de su fuente y cambiarlo tocaría seis temporadas de
tarjetas. Pero **hay que tenerlo en cuenta para cualquier cruce entre el circuito interno y el CSC**,
y para el importador de 2027. De paso, `campos.json` escribe **`Naturavila` sin tilde** solo en las
barras Azules, y `Naturávila` con tilde en las otras tres.

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
vuelta. Sólo afecta a la etiqueta del calendario: los puntos y los ups se han escrito con el equipo
correcto.

> **Rectificado el 2026-10-22.** Aquí se escribió que el título del acta («FORO 2000 VS APPROACH Y
> PUTT») demostraba que la fila de la jornada 5 era la del revés. **No lo demuestra:** el acta del ES6
> se titula «6. CUARTILLOS VS CLUB EL ESTUDIANTE» y en esa jornada el local era Club El Estudiante.
> El orden de los nombres en el título no dice quién es local. Ver el pendiente nº 5.

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

**Eliminados en cuartos.** El 20 de octubre, en El Encín, **Goldfers 2,5 – Cuartillos 1,5** (7 ups a
3). Individuales 1-1 —Aguirre gana 3&2, Buendía pierde 5&4— y fourball 0,5-1,5 —Montoya y Chiralt
empatan, Nacho González y Sequera pierden 2UP—. **La temporada de entre semana termina aquí.**

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

### 4. Falta el rival de cuartos de fin de semana

El de entre semana ya se sabe y se jugó: era **Goldfers**. Falta **quién gana el Grupo 1 de fin de
semana** (Golf de Golfos, Tres Cantos, CG Caminos y Grow Golf), que es contra quien jugamos el 15 de
noviembre. En `csc.json` el `FSQF` lleva `rival` puesto a `1º del Grupo 1 (cuartos)`; cuando se sepa,
se cambia esa cadena y se sube `CV`, nada más.

Del PDF federativo de `fuentes/` solo salen las jornadas hasta el 13 de junio de ese grupo: faltan
las del 27/09 y el 04/10, que no tenemos.

### 5. El `local` de fin de semana no es de fiar, y el título del acta tampoco lo arregla

**En entre semana las seis filas de `partidos_grupo` alternan local y visitante en las seis
parejas**, o sea que son coherentes entre sí. El campo `local` del partido las contradecía en ES1 y
ES5, y **esos dos se han corregido** el 2026-10-22.

**En fin de semana no.** Ahí **cuatro de las seis parejas tienen el mismo local en la ida y en la
vuelta**, así que el fallo está en las propias filas de grupo y no se puede deducir cuál de las dos
es la mala. **No se ha tocado nada**: haría falta el acta de cada jornada.

**Y una corrección de lo que se escribió el 2026-10-01.** Al cargar la jornada 5 de fin de semana se
dio por hecho que el título del acta («FORO 2000 VS APPROACH Y PUTT») decía quién era el local. **No
lo dice**: el acta del ES6 se titula «6. CUARTILLOS VS CLUB EL ESTUDIANTE» y en esa jornada el local
era Club El Estudiante. El número de delante es el orden del partido dentro de la agrupación, y el
orden de los nombres no significa nada. Así que aquella fila **no está demostrada del revés**, solo
es una más de las que no cuadran.

Esto solo afecta a la etiqueta LOCAL/VISITA del calendario. Puntos, ups y clasificación van aparte y
están bien.

### 6. ¿Están los tres nuevos de fin de semana comunicados a la RFGM?

El 2026-10-22 se dieron de alta en `modalidades[FS].elegibles` de `csc.json` a **Jaime Villanueva,
Marcos Ruiz y Nicolás Sequera**, por criterio de Álvaro: el que no está en la lista de entre semana
va a la de fin de semana. La lista pasa de 26 a **29 de los 30** que permite el §3.

**Pero esa es nuestra lista, no la que vale.** La que decide quién puede jugar es la que tenga la
federación: el §3 exige «estar en la lista de elegibles enviada en la inscripción», y el §11 que las
ampliaciones se manden a `competiciones@fedgolfmadrid.com`. **Falta confirmar que se ha comunicado.**

Hasta entonces hay una trampa abierta: **en el microsite ya pueden apuntarse**, porque el botón de
Apuntarme mira esta lista. Si no constan en la RFGM, podrían salir convocados y no poder jugar. Si
se confirma que no se ha comunicado, lo prudente es sacarlos de `elegibles` hasta que se haga.

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
