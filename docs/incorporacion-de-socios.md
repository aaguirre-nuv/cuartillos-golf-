# Cómo se incorporan los puntos de un socio nuevo

Escrito el **2026-09-11** al incorporar a Marcos Ruiz y Nicolas Sequera. Hasta ahora la regla no
estaba escrita en ninguna parte: vivía en la memoria de quien llevaba la clasificación.

## La regla

Cuando alguien que jugó un torneo **sin ser socio** se incorpora después al club, se le reconocen los
puntos de ese torneo **sin quitárselos a nadie**. En concreto:

- Se le asigna el puesto que le habría correspondido por su resultado (`difNeto`), y **los puntos de
  ese puesto**.
- **Todos los demás conservan el puesto y los puntos que ganaron el día del torneo.** Nadie baja de
  posición ni pierde puntos por la incorporación.
- La consecuencia visible es que en ese torneo **hay dos jugadores con el mismo `rankingSocios` y los
  mismos puntos**. No es un error del dato: es la firma de una incorporación.

## CORRECCIÓN del 2026-09-11

> La primera versión de este documento afirmaba que **no había precedente en 2024** y que el recuerdo
> de Álvaro sobre Juan Sanz no se sostenía. **Era falso, y la culpa fue del método de búsqueda.**
>
> Se buscó la firma equivocada: **puestos repetidos** (`rankingSocios` duplicado). Así se hizo en 2026,
> pero en 2024 se hizo al revés — **los puestos se renumeraron y lo que se repite son los puntos**—, de
> modo que el barrido no podía encontrarlo. El precedente existe, es de 2024, y es de Juan Sanz.
>
> Lo encontró Álvaro mirando los ficheros a mano. La firma correcta es **puntos repetidos dentro de un
> mismo torneo**, y con ella sale a la primera.

## Lo que dicen los datos

La escala de puntos es **fija por tipo de torneo** y estrictamente decreciente, así que dos jugadores
con los mismos puntos en el mismo torneo es siempre una anomalía:

| Tipo | Escala por puesto |
|---|---|
| 2 | 500 · 300 · 190 · 135 · 110 · 100 · 90 · 85 · 80 · 75 · 70 · 65 · 60 · 57 · 55 · 53 · 51 · 49 · 47 · 45 · 44 · 43 |
| 3 | 600 · 330 · 210 · 150 · 120 · 110 · 100 · 94 · 88 · 82 · 77 · 72 · 68 · 64 · 61 · 59 · 57 · 55 · 53 · 51 · 50 · 49 |

Buscados los puntos repetidos entre jugadores con puntuación en **todas** las temporadas:

- **2021, 2022, 2023 y 2025: ningún caso.**
- **2024: cuatro casos.**
- **2026: dos casos**, los dos en el torneo 7, que son Marcos Ruiz y Nicolas Sequera.

### El precedente de Juan Sanz, confirmado

Juan Sanz figura como socio (`tipoParticipacion: Si`) desde **2024**, y los dos ajustes están en los
dos primeros torneos que jugó, **seguidos, el mismo fin de semana**:

| Torneo | Qué pasó |
|---|---|
| **2024:4 · Saldaña · 18/05/2024** | Empató a `difNeto` 13 con Nacho González, que era 16º con **59** puntos. A Juan Sanz se le dan también **59** —el valor del puesto 16, no los 57 que marcaba el 17º— y **Nacho González conserva sus 59**. Por debajo, Touceda y Javier González Salvador bajan un puesto pero **mantienen los 57 y 55 que ganaron ese día**. |
| **2024:5 · Lerma · 19/05/2024** | Hizo `difNeto` −4, mejor que el −2 de Javier Arcos, que había **ganado el torneo** con 500 puntos. A Juan Sanz se le da el 1er puesto con **500**, y **Javier Arcos conserva sus 500** aunque pase a figurar 2º. El 3º sigue con sus 300. |

En los torneos 6, 8 y 9 de 2024 no hay ninguna anomalía, coherente con que a partir de junio ya fuera
socio de pleno derecho y no hiciera falta ajuste retroactivo.

### Los otros dos casos de 2024, sin explicar

El mismo mecanismo aparece dos veces más esa temporada, pero **con jugadores que ya eran socios de
antes**, así que no son incorporaciones y no se sabe desde aquí a qué respondieron:

- **2024:3 · Cabanillas:** Ruslan Kochman, 17º, cobra **53** en vez de los 51 del puesto, los mismos
  que Antonio Carmona en el 16º. Kochman era socio desde 2022.
- **2024:7 · Palomarejos:** Carlos Maestro, 17º, cobra **59** en vez de 57, los mismos que Javier
  Cervera en el 16º, y los de abajo bajan un puesto conservando sus puntos. Maestro era socio desde
  2023.

Hay además en **2024:3** una rareza distinta y sin relación con esto: entre tres empatados a
`difNeto` 5, el 3º cobra 135 y el 4º cobra 190, o sea los puntos cruzados respecto al puesto.

### Una diferencia de forma entre 2024 y 2026

El resultado en puntos es idéntico, pero el campo del puesto se llevó distinto: **en 2024 se
renumeraron los puestos** de los de abajo (quedan únicos, y lo que se repite son los puntos),
mientras que **en 2026 no se renumeraron** (GLEZ sigue siendo 15º con Nicolas Sequera también 15º).
No afecta a ningún punto ni a la clasificación general; solo a lo que se ve en el detalle del torneo.

## La incorporación de 2026: Marcos Ruiz y Nicolas Sequera

Torneo 7, **Desert Springs / Aguilón, 18 y 19 de julio de 2026**, a dos vueltas.

| Jugador | difNeto | Puesto que ocupa | Puntos | Con quién comparte puesto |
|---|---|---|---|---|
| Marcos Ruiz | 10 | 7º | **90** | Javier Arcos, que también hizo 10 y conserva sus 90 |
| Nicolas Sequera | 21 | 15º | **55** | GLEZ JUAN JOSÉ, que hizo 23 y conserva su 15º puesto y sus 55 |

Nadie perdió nada. Si en lugar de esto se hubiera recalculado el torneo, habrían bajado un puesto
**GLEZ JUAN JOSÉ, Enrique Gonzalez R, J. Enrique Gonzalez, José Pablo Guil, David Sequera y Juan
Sanz**, además de dejar a Javier Arcos o a Marcos en 85 puntos por el empate.

En la clasificación general de 2026 eso deja a **Marcos Ruiz 34º con 90 puntos** y a **Nicolas Sequera
37º con 55**, cada uno con **+1 golpe de ventaja** para el torneo final (1 golpe por cada 100 puntos).

## La trampa que costó encontrar el fallo

Que un jugador tenga sus puntos en el dato **no basta** para que el microsite los enseñe. La
clasificación general mira el campo **`sinEquipo`** de `datos/clas_matrix_<año>.json`: si está en
`true`, la fila sale en gris y en cursiva, con la etiqueta «sin equipo», y **oculta el puesto, todos
los puntos por torneo, el total y el golpe de ventaja**. Aunque los puntos estén guardados.

El 2026-09-10 se corrigió ese campo a `false` para los dos, pero el fichero se guardó como
**`clas matrix 2026.json`, con espacios en vez de guiones bajos**. El microsite lee
`clas_matrix_2026.json`, así que la corrección nunca llegó a la página: los dos seguían saliendo sin
puntos. Los dos ficheros eran idénticos **salvo en ese único campo**. Corregido el 2026-09-11 sobre el
fichero bueno, y eliminado el duplicado.

**Para incorporar a alguien hay que tocar tres sitios**, y olvidar el tercero no da ningún error:

1. `datos/clasificacion_<año>.json` — su resultado del torneo, con `puntos`, `rankingSocios` y
   `tipoParticipacion: "Si"`.
2. `datos/clas_matrix_<año>.json` — su fila en la clasificación general, con `torneos`, `total`, `rk` y
   **`sinEquipo: false`**.
3. `microsite.html` — subir la variable `CV`, o los navegadores que ya han visitado la página seguirán
   sirviendo los datos viejos.

`datos/jugadores.json` **no** hace falta: ese fichero se dejó de mantener en 2025 y no tiene ninguna
fila de 2026.

## Juan Sanz en 2026: se queda como está

**Juan Sanz sigue marcado con `sinEquipo: true`** en 2026, así que sus 45 puntos del torneo 7 están
guardados pero **no se ven** en la clasificación general: su fila sale en gris con la etiqueta «sin
equipo». Fue socio con equipo en 2024 y 2025 (CUATREROS GC) y este año no tiene equipo asignado.

**Decisión de Álvaro del 2026-09-11: «Juan Sanz viene así». No se toca.** No es un fallo pendiente, es
el estado correcto: quien lo vea en gris en la clasificación de 2026 no tiene que arreglar nada.
