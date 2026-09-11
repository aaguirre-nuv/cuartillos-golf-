# Contexto del repo · Microsite del Club de Golf Cuartillos

Repo personal (no es un proyecto de cliente de Nuvirta). Contiene el **microsite del club**, una única
página estática que se sirve tal cual y lee ficheros JSON de la carpeta `datos/`.

## Qué hay

- `microsite.html` — la aplicación entera: maquetación, estilos y JavaScript en un solo fichero.
  Secciones: portada, calendario, clasificación, equipos, tarjetas, jugador, estadísticas y **CSC**.
- `datos/` — los datos, en JSON por temporada (2021 a 2026):
  - `jugadores.json`, `handicaps.json`, `calendario.json`, `campos.json`, `estadisticas.json`.
  - `tarjetas_<año>.json` y `clasificacion_<año>.json` — resultados hoyo a hoyo y por torneo.
  - `clas_matrix_<año>.json` — clasificación general del circuito interno.
  - `equipos_clasificacion_<año>.json` — clasificación por equipos del circuito interno.
  - `csc.json` — la participación en las **Ligas de Clubes sin Campo de la RFGM**: modalidades `ES`
    (entre semana) y `FS` (fin de semana), con elegibles, partidos, resultados y ups.
- `img/` — logo del club y escudos de los equipos del circuito interno.
- `docs/` — documentación del proyecto y fuentes originales.

## Dos competiciones distintas, que no hay que mezclar

1. **El circuito interno del club** (torneos propios, equipos como «Gimbros» o «Cerdos Arqueros»,
   clasificación por puntos y golpes de ventaja para el torneo final). Es la mayor parte del microsite.
2. **Las Ligas de Clubes sin Campo (CSC) de la Real Federación de Golf de Madrid**, donde Cuartillos
   compite contra otros clubes. Reglamento propio, ajeno al club, y con dos ligas independientes.
   Vive en `datos/csc.json` y en la sección CSC del microsite.

## Incorporación de socios y puntos del circuito interno

Cómo se reconocen los puntos de alguien que jugó un torneo sin ser socio y se incorpora después, qué
hay que tocar para que aparezca en la clasificación, y por qué tener los puntos en el dato **no basta**
para que se vean: [`docs/incorporacion-de-socios.md`](docs/incorporacion-de-socios.md).

## Reglamento CSC 2026

Las reglas de la competición federativa —formatos, golpes de ventaja, límites de hándicap, listas de
elegibles, desempates, inscripciones y plazos— están resumidas en
[`docs/reglamento-csc-2026.md`](docs/reglamento-csc-2026.md), con el PDF original de la circular en
`docs/fuentes/`. **Antes de tocar nada de la sección CSC o de `datos/csc.json`, leer ese documento**:
el formato de los partidos y el número de jugadores por equipo no son iguales en las dos ligas, y
dependen de cuántos equipos se clasificaron.
