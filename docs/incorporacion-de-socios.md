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

## Lo que dicen los datos, y lo que no

Buscada la firma —puestos repetidos dentro de un mismo torneo— en **todas** las temporadas de
`datos/clasificacion_*.json`:

- **2023, 2024 y 2025: ningún caso.** Ni uno.
- **2021 y 2022:** hay puestos repetidos, pero todos con `rankingSocios` **0 y 0 puntos**, que es como
  se marca a los no socios. No es lo mismo.
- **2026, torneo 7 (Desert Springs / Aguilón):** los dos únicos casos reales de toda la serie, que son
  precisamente Marcos Ruiz y Nicolas Sequera.

**Sobre el recuerdo de que esto se hizo el año en que se incorporó Juan Sanz:** no se ha encontrado
rastro de ello. Juan Sanz aparece como socio (`tipoParticipacion: Si`) desde **2024**, y en esa
temporada sus seis resultados tienen puestos distintos y consecutivos, sin ninguna posición repetida;
tampoco tiene resultados anteriores a su alta que se le hayan recuperado, ni hay nada suyo en 2023.

Lo que sí hay es esto: en **este mismo torneo 7 de 2026** Juan Sanz tiene 45 puntos con
`tipoParticipacion: Si`, y entró con el propio torneo, no después. Como quedó **el último**
clasificado (`difNeto` 40), reconocerle los puntos **no desplazaba a nadie**, así que su caso no deja
la firma de puestos repetidos aunque siga la misma regla. **La práctica es la que se recordaba; el año
y el jugador, no.**

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

## Pendiente de decidir

**Juan Sanz sigue marcado con `sinEquipo: true`**, así que sus 45 puntos del torneo 7 están guardados
pero **no se ven** en la clasificación general: su fila sale en gris con la etiqueta «sin equipo». Fue
socio con equipo en 2024 y 2025 (CUATREROS GC) y este año no tiene equipo asignado. Si debe verse como
los otros dos, basta con poner ese campo a `false`. **Sin decidir a propósito**: no se sabe desde aquí
si este año es socio o no.
