# Estado del proyecto

**Al 2026-09-11.** Los estados anteriores están en el historial de git.

---

## Lo primero al volver

**Mañana, sábado 2026-09-12, se juega el torneo 8 en La Faisanera**, del circuito interno. Es de
**tipo 3**, o sea que reparte la escala alta: 600 al ganador, luego 330, 210, 150, 120, 110, 100, 94…
En el calendario figura con `jugado: 0` y sin hora, tee ni salidas.

Antes de cargar sus resultados hay **una cosa sin resolver**: ver «Alta de Marcos y Nicolas» abajo.

## Qué se hizo el 2026-09-11

### Ligas de Clubes sin Campo (CSC)

- Incorporado el **reglamento 2026** (Circular 26/2026 de la RFGM) al repo, resumido en
  [`reglamento-csc-2026.md`](reglamento-csc-2026.md) con los PDF originales en `fuentes/`.
- Cerrada la **jornada 5 de entre semana**: Cuartillos gana 4-2 a Grow Golf en Montealvar, 18 ups a
  favor y 7 en contra. Con la ida ganada 2-1, el enfrentamiento cae 6-3 y suma 1 punto de liga.
- Incorporados los dos **PDF de resultados acumulados** de la RFGM (entre semana y fin de semana) y
  contrastados fila a fila con `datos/csc.json`.
- **Tres cifras alineadas con el acta federativa** por decisión de Álvaro: ver §13.2 del reglamento.
  Cuartillos queda en **20 ups a favor y 13 en contra** en fin de semana.
- **Eliminado el campo `clasificacion` de la modalidad FS**: era un derivado que el microsite ya
  recalcula desde `partidos_grupo`. La clasificación de un grupo se calcula, no se guarda.

### Circuito interno

- **Marcos Ruiz y Nicolas Sequera ya se ven en la clasificación**: 34º con 90 puntos y 37º con 55, los
  dos con +1 golpe de ventaja. El dato estaba bien desde el día 10; lo que fallaba es que el campo
  `sinEquipo` seguía en `true`, y con eso el microsite oculta puesto, puntos, total y golpes.
- La corrección del día 10 se había guardado en un fichero llamado **`clas matrix 2026.json`, con
  espacios**, que el microsite no lee. Aplicada sobre `clas_matrix_2026.json` y borrado el duplicado.
- Documentada en [`incorporacion-de-socios.md`](incorporacion-de-socios.md) la regla de reconocer
  puntos a un socio nuevo **sin quitárselos a nadie**, con el precedente de Juan Sanz en 2024
  confirmado, la escala de puntos por tipo de torneo, y los tres sitios que hay que tocar.

### Microsite

- **Subida la versión de caché** (`CV`) y **unificadas las tres URL de datos** que estaban escritas a
  mano con versiones distintas entre sí. Antes, el mismo fichero se cacheaba por dos URL diferentes
  según por dónde se entrara a la sección CSC. `CV` se declara ahora junto a `BASE`, arriba del todo,
  porque una de esas cargas corre en un IIFE que se ejecutaba antes de la declaración anterior.

## Estado actual, frente por frente

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

Redactado un mensaje de WhatsApp para animar a apuntarse al 27. **La inscripción abre el lunes
2026-09-14 a las 10:00 y cierra el lunes 2026-09-21 a las 10:00**, por la web de la RFGM, 48 €.

### Circuito interno · plantillas de 2026

**La tabla de miembros de cada equipo existe, y está en el Excel `datos/TodasDimensiones.xlsx`, hoja
«Jugadores por EquipoAño».** El microsite **no la lee**: tira de `datos/jugadores.json`, que se dejó
de generar en 2025 y **no tiene ni una fila de 2026**. Por eso desde los datos publicados solo se
puede reconstruir quién ha jugado, que no es lo mismo que quién está fichado.

| Equipo | Fichados | Aún no han jugado en 2026 |
|---|---|---|
| Gimbros | 7 | Juan Jose Aguado |
| No Te La Lleves Mamado | 6 | Javier López Gullón |
| Cerdos Arqueros | 5 | Nacho González |
| La Orden del Swing Sagrado | 5 | — |
| Los Guardianes del Datáfono | 5 | — |
| Me Alivio Golf Club | 5 | — |
| La Amenaza Fantasma | 5 | — |

Son **38 en equipo más tres socios sin equipo**: Franck Benouniche, Jaime de la Cal y Juan Sanz.

**Juan Sanz sale en gris con la etiqueta «sin equipo» y eso es correcto**, decisión de Álvaro del
2026-09-11: «Juan Sanz viene así». No es un fallo pendiente.

## Pendiente

### 1. Alta de Marcos y Nicolas en el origen · antes del torneo de mañana

**No están en el Excel**, ni en la hoja `Jugadores` ni en `Jugadores por EquipoAño`. Lo hecho los días
10 y 11 tocó solo los ficheros de salida (`clasificacion_2026.json`, `clas_matrix_2026.json`,
`tarjetas_2026.json`), no la fuente.

Hace falta que Álvaro diga **en qué equipo juega cada uno**. Mientras no lo tengan:

- En la clasificación **individual** ya salen bien, con sus puntos y su golpe de ventaja.
- En la clasificación **por equipos** sus puntos **no suman a nadie**.

### 2. Regenerar `jugadores.json` para 2026

Desde la hoja «Jugadores por EquipoAño» del Excel, para que el microsite vuelva a conocer las
plantillas y la pregunta «cuántos jugadores tiene cada equipo» se pueda contestar sin abrir el Excel.
Propuesto, no aprobado.

### 3. Dudas abiertas, sin urgencia

- **Dos ajustes de puntos de 2024 sin explicar**, con el mismo mecanismo de la incorporación pero
  sobre socios antiguos: Ruslan Kochman en Cabanillas y Carlos Maestro en Palomarejos. Detalle en
  [`incorporacion-de-socios.md`](incorporacion-de-socios.md).
- **En el torneo 3 de 2024**, entre tres empatados a `difNeto` 5, el 3º cobra 135 y el 4º cobra 190:
  los puntos cruzados respecto al puesto.
- **El PDF federativo de fin de semana se contradice en una celda** (Foro 2000 – Putt & Drive: da ida
  12-0 y vuelta 5-1 en ups pero totaliza 17-2). No afecta a Cuartillos.

## Tres trampas de este repo, aprendidas hoy a base de tropezar

1. **Cambiar un dato no basta: hay que subir `CV` en `microsite.html`.** Si no, los navegadores que ya
   han visitado la página siguen sirviendo la copia vieja, y el dato parece mal cuando está bien.
2. **Un dato correcto puede no verse.** El campo `sinEquipo` a `true` oculta puesto, puntos, total y
   golpes de ventaja de esa fila entera.
3. **El Excel es la fuente; los JSON son la salida.** Corregir solo el JSON deja el origen mal, y la
   próxima regeneración se lleva la corrección por delante.
