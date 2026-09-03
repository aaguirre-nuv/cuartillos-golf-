# Registro de decisiones

Una entrada por decisión. Cada una dice qué se decidió, en qué se apoya y qué
consecuencia tiene. Las decisiones **pendientes** están al final y no deben
aplicarse hasta que se cierren.

Convenciones:

- **Decidida** — acordada y aplicable.
- **Pendiente** — hace falta una respuesta antes de poder aplicarla.
- **Evidencia** — lo que sostiene la decisión. Si la evidencia es sólo el dato
  histórico, se dice; si viene del reglamento, se cita.

---

## D-001 · Los cambios en `datos/` requieren OK explícito

**Estado:** decidida · 2026-09-03

Ninguna modificación de `datos/` se aplica sin autorización expresa y por
escrito para ese cambio concreto. El análisis, la auditoría y la documentación no
la necesitan.

**Motivo:** el microsite lee `datos/` por ruta relativa
(`microsite.html:301`, `var BASE='./datos/'`), así que un cambio en esos ficheros
publicado en la rama que sirve la web sale publicado sin paso intermedio de
revisión.

**Consecuencia:** las correcciones descritas en [DIFERENCIAS.md](DIFERENCIAS.md)
están documentadas pero **no aplicadas**.

---

## D-002 · El trabajo se desarrolla en rama, no en `main`

**Estado:** decidida · 2026-09-03

Los cambios se preparan en una rama, se revisan y sólo entonces pasan a `main`.

**Motivo:** el repositorio tiene un solo autor y un historial lineal sobre `main`
sin PRs previos, pero los cambios de datos tocan varios ficheros que tienen que
quedar coherentes entre sí y no se ven a simple vista.

---

## D-003 · Criterio de desempate de posiciones

**Estado:** decidida · 2026-09-03 · **con fuente documental**

Se aplica el criterio **RFEG (Libro Verde)** para prueba hándicap Stroke Play,
ganando siempre el **menor** número de golpes:

1. Resultado neto del torneo (suma de las rondas si es a doble vuelta).
2. **Hándicap de juego más bajo**. El de juego, no el exacto.
3. Golpes **netos** en los últimos **9, 12, 15, 16 y 17** hoyos, en ese orden.
4. Si persiste el empate, **sorteo**.

Los "últimos hoyos" son los últimos **del campo**, no los últimos que jugó cada
participante: con salida a tiro el cálculo no cambia.

**Fuente:** [`reglamento/2026-T6-layos-resolucion-desempate.pdf`](reglamento/2026-T6-layos-resolucion-desempate.pdf),
resolución del desempate del T6 de 2026 (Layos, 27 de junio de 2026).

**Verificación:** la regla reproduce 1.083 de los 1.097 puestos de socio de
2021-2026. Los datos del repositorio reproducen el cálculo del documento hoyo
por hoyo: Luis Fernández y David Sequera, empatados a +1 neto con hándicap de
juego 14 los dos, suman 0 y 0 en los hoyos 10-18, y +3 contra −1 en los hoyos
7-18.

**Evidencia adicional del dato:**

- Sin el hándicap de juego la regla acierta 378 puestos en vez de 1.079. El
  reglamento y el dato coinciden en que es el primer desempate.
- "Menos golpes gana": la variante inversa pierde unos 30 puestos.
- Bruto o neto en el *match of cards* da el mismo orden en los 31 grupos de
  empate de las seis temporadas, porque con el mismo hándicap de juego en el
  mismo campo se diferencian en una constante. El reglamento dice neto y es lo
  que se usa.

**Corrección de una decisión anterior:** durante el análisis se adoptaron
sucesivamente los órdenes 3 → 6 → 9 y 9 → 6 → 3, ninguno de los dos correcto.
Los tramos del reglamento son 9, 12, 15, 16 y 17, y el orden supuesto era la
causa de que el T6 de 2026 pareciera un error del dato cuando el dato era
correcto. De ahí la norma de estos documentos: ninguna regla se da por buena sin
fuente documental.

**Consecuencia:** los históricos **no se recalculan**. La regla se aplica a
torneos nuevos.

## D-004 · Incorporación de un invitado como socio: cómo se le otorgan puntos

**Estado:** decidida, con precedente documentado

Cuando un jugador que compitió como invitado pasa a socio **dentro de la misma
temporada**, se le otorgan puntos de los torneos que ya jugó con este método:

- El jugador entra en su **posición real** dentro del ranking de socios.
- Recibe **los mismos puntos que el socio inmediatamente por delante** (o los
  del campeón, si él resulta primero).
- **Ningún socio pierde puntos**: los que quedan por debajo conservan
  exactamente los puntos de la posición que tenían antes de la incorporación.

Consecuencia asumida: el torneo reparte un tramo de puntos de más. Es el precio
de no desvirtuar el resultado real ya publicado.

**Evidencia** — cuatro casos en 2024, todos con la misma firma (puntos que se
desvían de la escala sólo desde la posición del incorporado hacia abajo, cada
socio conservando los puntos de su puesto previo):

| Torneo | Jugador | Puesto | Puntos recibidos | Escala de ese puesto |
|---|---|---|---|---|
| 2024 T3 Cabanillas (Normal) | Ruslan Kochman | 17.º | 53 | 51 |
| 2024 T4 Saldaña (Major) | **Juan Sanz** | 17.º | 59 | 57 |
| 2024 T5 Lerma (Normal) | **Juan Sanz** | 1.º | 500 | 500 |
| 2024 T7 Palomarejos (Major) | Carlos Maestro | 17.º | 59 | 57 |

El caso más claro es **2024 T5 Lerma**: Juan Sanz ganó el torneo con 68 netos y
recibió 500 puntos, y Javier Arcos (70 netos) **mantuvo sus 500 puntos y su
victoria**. Los 20 socios de la tabla conservaron sus puntos íntegros.

**Contraprecedente, igual de importante:** Thomas Dauterman jugó como invitado
los mismos torneos de 2024 (T4, T5 y T11) y **no** recibió puntos por ellos. Sus
tarjetas siguen con `rk: null` y `pts: null` y no aparece en
`clasificacion_2024.json`. Estaba dado de alta como `"Inv"` en la temporada 2024
y como `"Si"` a partir de 2025, y empezó a puntuar en el T1 de 2025.

**Regla que distingue los dos casos:** lo que decide no es haber jugado como
invitado, sino **para qué temporada se da de alta al jugador como socio**. Juan
Sanz figura `"Si"` en 2024 y recibió puntos desde su primer torneo de esa
temporada; Thomas Dauterman figura `"Inv"` en 2024 y `"Si"` en 2025, y empezó a
puntuar en 2025.

---

## Pendientes

### P-001 · Confirmar el orden del *match of cards* — **CERRADO** 2026-09-03

Resuelto con la resolución del T6 de 2026. Ver D-003. Los tramos son 9, 12, 15,
16 y 17 hoyos, no 9-6-3 ni 3-6-9.

Queda como derivada, de menor alcance: verificar con qué criterio estaban
configurados en la plataforma los 6 torneos con desempates invertidos que lista
[DIFERENCIAS.md](DIFERENCIAS.md), punto 5.

### P-002 · Nicolás Sequera y Marcos Ruiz: temporada de alta

Ambos jugaron el 2026 T7 (Desert Springs / Aguilón) como invitados. Hay que
decidir, según D-004, si se dan de alta como socios **de 2026** —y entonces les
corresponden puntos del T7— o **de 2027**, y entonces el T7 se queda sin puntos
para ellos.

Si se decide 2026, los puntos que salen de aplicar D-004 son:

| Jugador | Puesto entre socios | Puntos | Referencia |
|---|---|---|---|
| Marcos Ruiz | 8.º | **90** | mismos que Javier Arcos, 7.º, con el que empata a 152 netos |
| Nicolás Sequera | 16.º | **57** | mismos que Nacho Casas, 15.º |

Ningún socio pierde puntos. En la general de 2026 quedarían 34.º con 90 y 37.º
con 57.

### P-003 · Nicolás Sequera y Marcos Ruiz: equipo

Sus tarjetas tienen `equipo: null` e `idTempEquipo: null`.

**Advertencia:** asignarles equipo **cambia la clasificación por equipos del T7
ya publicada**, porque el `teamScore` es la suma por ronda de los 2 mejores
`difNeto` del equipo y los dos entrarían entre esos 2 mejores en Aguilón (ambos
firmaron +3). Efecto calculado sobre el T7, por equipo:

| Equipo | teamScore actual | Con Marcos | Con Nicolás | Asistencia |
|---|---|---|---|---|
| LOS GUARDIANES DEL DATÁFONO | +5 | +4 | +4 | 150 → 150 |
| LA ORDEN DEL SWING SAGRADO | +14 | +10 | +10 | 100 → 150 |
| LA AMENAZA FANTASMA | +16 | +9 | +9 | 60 → 100 |
| CERDOS ARQUEROS | +27 | +19 | +19 | 60 → 100 |
| NO TE LA LLEVES MAMADO | +39 | +23 | +30 | 30 → 60 |
| ME ALIVIO GOLF CLUB | +44 | +25 | +36 | 30 → 60 |

Mejor score y más puntos de asistencia pueden cambiar el `ranking` del torneo y,
con él, los `puntosEquipos` de **todos** los equipos.

### P-004 · Dónde se declara que un jugador es socio en 2026

`jugadores.json` sólo cubre 2020-2025. Hay que decidir si se extiende a 2026 o si
el estado de socio se queda en los ficheros derivados (`invitado` en tarjetas y
`tipoParticipacion` en clasificación), que es de donde lo lee el microsite.

### P-005 · Correcciones de datos propuestas y no aplicadas

Cada una está documentada en [DIFERENCIAS.md](DIFERENCIAS.md) con su evidencia y
su impacto. Requieren OK una por una:

| # | Corrección | Afecta a |
|---|---|---|
| 1 | Javier Dodero es invitado, no socio, en 2026 T2 | 3 socios ganan entre 1 y 2 puntos |
| 2 | Puntos cruzados del 3.º y 4.º en 2024 T3 | Angel Santana +55, Javier González −55 |
| 4 | Cola de puntos del 2026 T5 (puestos 21 a 24) | 4 socios ganan entre 1 y 3 puntos |
| 3 | Unificar la fórmula de puntos de asistencia de equipos | puntos de equipo de 2026 T4, T5 y T6 |
| 6 | Decidir si la Final de 2024 debía repartir puntos | general de 2024 completa |
