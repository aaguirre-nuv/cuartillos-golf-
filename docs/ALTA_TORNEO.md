# Alta de un torneo nuevo: comprobaciones

Lista de comprobación para cada torneo que se incorpora. **No documenta cómo se
genera el dato** —de dónde salen las tarjetas y con qué herramienta se cargan no
está registrado en el repositorio y no se ha verificado**`[NO VERIFICADO]`**—
sino qué tiene que cumplirse una vez cargado.

Cada comprobación indica el fichero y la regla, y todas las reglas están
verificadas contra el histórico en [MODELO.md](MODELO.md).

## 1. Calendario

- [ ] El torneo existe en `calendario.json` con `temporada`, `nTorneo`, `fecha`,
      `campo`, `parTotal` y `tipoTorneo` (1 The Final, 2 Normal, 3 Major).
- [ ] `jugado` pasa a `1`.
- [ ] `nTornPunt` está relleno: es cuántos resultados cuentan para la general a
      partir de este torneo. Determina el `nPunt` de todos los jugadores.
- [ ] Si es a doble vuelta: `fechaFin`, `campoR1`, `campoR2`, `parR1`, `parR2`, y
      `parTotal` igual a la suma de los pares de las dos rondas.

## 2. Tarjetas

- [ ] Una tarjeta por jugador y **por ronda** en `tarjetas_YYYY.json`.
- [ ] El objeto `hoyos` está completo, con `b` (bruto), `n` (neto), `p` (par) y
      `c` (categoría) en los 18 hoyos. **Sin esto no se puede desempatar.**
- [ ] Los invitados llevan `invitado: true`, `pts: null` y su `rk` en la escala
      **general** del torneo (todos los jugadores, socios e invitados).
- [ ] Los socios llevan su `rk` en la escala **de socios** (sólo socios). Las dos
      escalas conviven, así que ver un mismo `rk` repetido en un torneo con
      invitados es normal.

## 3. Posiciones y desempate

- [ ] El ranking de socios se ordena con el criterio **RFEG (Libro Verde)**:
      neto, hándicap de juego más bajo, y *match of cards* sobre golpes netos en
      los últimos **9, 12, 15, 16 y 17** hoyos. **Menor gana en todos los pasos.**
- [ ] Los "últimos hoyos" son los últimos **del campo** (últimos 9 = hoyos 10-18,
      últimos 12 = hoyos 7-18, y así). Con salida a tiro **no** son los últimos
      que jugó cada uno.
- [ ] A doble vuelta: el neto es la suma de las rondas, el handicap de juego es
      la **suma** de las rondas y el countback se toma de la **última ronda**.
- [ ] Comprobar que el torneo estaba **configurado con criterio RFEG** en la
      plataforma de resultados. Es un ajuste por torneo, y hay 7 parejas del
      histórico donde el desempate salió al revés (ver
      [DIFERENCIAS.md](DIFERENCIAS.md), punto 5).
- [ ] Si un empate llega al *match of cards*, dejar constancia del cálculo. El
      dato guardado no permite reconstruirlo por sí solo, y una resolución
      escrita como la del T6 de 2026 es lo que zanja las dudas después.
- [ ] Si el empate persiste tras los cinco tramos, se resuelve por **sorteo**, y
      hay que registrarlo: el dato no puede reflejarlo de otra forma.

## 4. Puntos individuales

- [ ] Los puntos se asignan por `rankingSocios`, **nunca** por `posicionTorneo`.
- [ ] Se usa la escala del `tipoTorneo` correspondiente (tabla en
      [MODELO.md](MODELO.md#3-escala-de-puntos-individuales)).
- [ ] Los invitados no reciben puntos.
- [ ] Comprobación cruzada: el `pts` de la tarjeta y el `puntos` de la
      clasificación tienen que coincidir. En seis temporadas hay **una sola**
      excepción, y es un error (ver
      [DIFERENCIAS.md](DIFERENCIAS.md), punto 1).

## 5. Clasificación del torneo

- [ ] Una fila por **socio** y torneo en `clasificacion_YYYY.json`, incluso si el
      torneo fue a doble vuelta (una fila, no dos).
- [ ] Los invitados no entran. Si se decide incluirlos, con la forma que usa
      Javier Aguirre en 2026 T3: `tipoParticipacion: "Inv"`,
      `rankingSocios: 0`, `puntos: 0`.

## 6. Clasificación general

- [ ] En `clas_matrix_YYYY.json`, el torneo aparece en `torneos` de cada jugador
      que lo jugó.
- [ ] `nPunt` == `min(nTornPunt del torneo, nJugados)` para cada jugador.
- [ ] `computan` == los `nPunt` torneos de mayor puntuación de ese jugador.
- [ ] `total` == suma de los puntos de los torneos de `computan`.
- [ ] `rk` recalculado sobre los nuevos totales.

## 7. Clasificación por equipos

- [ ] `teamScore` == suma, por cada ronda, de los **2 mejores `difNeto`** del
      equipo en esa ronda. Menor es mejor.
- [ ] `computa: true` en los jugadores que entraron entre esos 2 mejores en
      alguna ronda. Si hay empate en el corte, la elección es indiferente para el
      score.
- [ ] `valid: false` si el equipo presenta menos de 2 jugadores. Esos equipos
      **siguen recibiendo** los puntos del último puesto.
- [ ] `puntosEquipos` según la escala por `ranking`: 500, 400, 300, 200, 175,
      150, 125, 100, 75.
- [ ] `puntosAsistencia` según la fórmula que se acuerde. **Hoy hay tres
      fórmulas distintas en el histórico** (ver
      [DIFERENCIAS.md](DIFERENCIAS.md), punto 3): hasta cerrar eso, dejar
      constancia en la bitácora de cuál se usó.
- [ ] `puntosTotales` == `puntosEquipos` + `puntosAsistencia`.
- [ ] Bloque `equipos`: `torneos`, `computan`, `nPunt`, `total` actualizados con
      la misma lógica de mejores N que la clasificación individual.

## 8. Si se incorpora un jugador nuevo

- [ ] Decidir **para qué temporada** se le da de alta como socio. Es lo que
      determina si recibe puntos de los torneos que ya jugó como invitado (ver
      [DECISIONES.md](DECISIONES.md), D-004).
- [ ] Si se le da de alta en la temporada en curso, aplicar D-004: entra en su
      posición real, recibe los puntos del socio inmediatamente por delante, y
      **ningún socio pierde puntos**.
- [ ] Si se le asigna equipo, recalcular la clasificación por equipos **de todos
      los torneos afectados**: entrar en un equipo puede cambiar su `teamScore`,
      su `ranking` y, en cascada, los `puntosEquipos` de los demás equipos.
- [ ] Anotar la incorporación en la bitácora y, si sienta criterio, en el
      registro de decisiones.

## 9. Cierre

- [ ] Revisar el diff antes de publicar: los cambios de datos tocan varios
      ficheros que tienen que quedar coherentes entre sí.
- [ ] Anotar el torneo en la [bitácora](BITACORA.md).
