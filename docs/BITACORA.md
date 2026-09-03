# Bitácora

Registro cronológico, de lo más reciente a lo más antiguo. Sirve para ver la
evolución: qué se analizó, qué se decidió, qué se cambió y qué se deshizo.

Cada entrada dice **qué se hizo** y **qué quedó en el dato**. Si un cambio se
revirtió, se deja constancia en lugar de borrar la entrada.

---

## 2026-09-03 (2) · Se incorpora el reglamento de desempates

**Origen:** aportación de la resolución oficial del desempate del T6 de 2026
(Layos), que fija el criterio aplicable.

**Qué cambia:** el criterio de desempate pasa de supuesto a documentado. Es
**RFEG (Libro Verde)**: neto, hándicap de juego más bajo, y *match of cards*
sobre golpes netos en los últimos **9, 12, 15, 16 y 17** hoyos; si persiste,
sorteo. Los tramos supuestos hasta ahora (9-6-3 y 3-6-9) eran **incorrectos los
dos**.

**Consecuencias:**

1. **El T6 de 2026 deja de ser una diferencia: el dato era correcto.** Figuraba
   como el error de mayor peso encontrado, 500 puntos contra 300 sin regla que lo
   explicase. La resolución documenta el cálculo y los datos del repositorio lo
   reproducen hoyo por hoyo: empate a +1 neto y a hándicap de juego 14, empate a
   0 en los hoyos 10-18, y −1 de David Sequera contra +3 de Luis Fernández en los
   hoyos 7-18. El error estaba en la regla supuesta, no en el dato.
2. **P-001 queda cerrado.** Ver D-003.
3. Las diferencias de desempate bajan de 9 parejas a **7**, y ninguna es ya del
   T6. La regla oficial reproduce 1.083 de los 1.097 puestos de socio.
4. Se confirma que el *match of cards* va sobre **netos** y que da igual usarlo
   con brutos, porque con el mismo hándicap de juego se diferencian en una
   constante.
5. Se añade una precisión que no estaba en ningún sitio: los "últimos hoyos" son
   los últimos **del campo**, no los últimos que jugó cada participante. Con
   salida a tiro el cálculo no cambia.

**Qué quedó en el dato:** **nada**. `datos/` sigue intacto.

**Se añade al repositorio:** la resolución, en
[`reglamento/2026-T6-layos-resolucion-desempate.pdf`](reglamento/2026-T6-layos-resolucion-desempate.pdf),
como fuente de D-003.

**Verificación de que las posiciones de Nicolás y Marcos no cambian:**
recalculado el T7 de 2026 con la regla oficial, Marcos Ruiz sigue **8.º** entre
socios y Nicolás Sequera **16.º**, con 90 y 57 puntos según D-004. El empate de
Marcos con Javier Arcos a 152 netos lo resuelve el hándicap de juego (21 contra
51), sin llegar al *match of cards*.

---

## 2026-09-03 · Auditoría del modelo y documentación inicial

**Origen:** consulta sobre en qué posición terminaron Nicolás Sequera y Marcos
Ruiz en el último torneo, con vistas a incorporarlos como socios.

**Qué se hizo:**

1. Se localizó el último torneo jugado: **2026 T7, Desert Springs / Aguilón,
   18-19 de julio de 2026**, a doble vuelta. El T8 (La Faisanera, 12 de
   septiembre) figura con `jugado: 0`.
2. Se determinaron sus posiciones: ambos jugaron como invitados, Marcos 9.º y
   Nicolás 17.º en la clasificación **general** (24 jugadores). Reordenados como
   socios serían **8.º** y **16.º**.
3. Se reconstruyó el precedente de incorporación de invitados a socios y se
   documentó como **D-004**, con cuatro casos de 2024 y el contraprecedente de
   Thomas Dauterman.
4. Se validó el criterio de desempate contra las 1.097 posiciones de socio de
   2021-2026, contrastando ocho variantes de la regla. Resultado en **D-003**.
5. Se auditó el modelo completo: escalas de puntos, clasificación general,
   clasificación por equipos, tratamiento de invitados y coherencia entre
   ficheros. Resultado en [MODELO.md](MODELO.md).
6. Se levantaron 11 diferencias e incoherencias, cada una con su evidencia y su
   impacto, en [DIFERENCIAS.md](DIFERENCIAS.md).

**Qué quedó en el dato:** **nada**. `datos/` está intacto.

**Cambio hecho y revertido:** se llegaron a añadir columnas de desempate (`u3`,
`u6`, `u9`, `desempate`, `hcpJuegoDesempate`) a los 12 ficheros de tarjetas y
clasificación de 2021-2026, en el commit `b05145f`. Se revirtió a petición
expresa: la rama volvió a `4c31e08` y se verificó por checksum que los ficheros
son idénticos a los de `main`. De ahí sale **D-001**: ningún cambio en `datos/`
sin OK explícito.

**Correcciones propuestas y no aplicadas:** las cinco de **P-005**. Ninguna
tiene autorización.

**Abierto al cerrar la entrada:** P-001 (orden del *match of cards*, cerrado
ese mismo día en la entrada siguiente), P-002 (temporada de alta de Nicolás y Marcos), P-003 (su equipo),
P-004 (dónde se declara el socio de 2026), P-005 (las correcciones).

### Hallazgos que conviene no perder de vista

- **El modelo actual no puede recalcular el desempate.** Los segmentos de 9, 6 y
  3 hoyos no existen como campo, y en torneos a doble vuelta `handicapJuego`
  guarda sólo el de la última ronda, no la suma que usa el desempate.
- **2026 T6 Layos** reparte 500 y 300 puntos entre dos jugadores empatados a
  neto, hándicap de juego y últimos 9 hoyos. *Anotado ese día como la diferencia
  de mayor peso; resuelto en la entrada siguiente: el dato era correcto y la
  regla supuesta era la equivocada.*
- **Asignar equipo a un jugador incorporado cambia clasificaciones por equipos ya
  publicadas**, porque el `teamScore` sale de los 2 mejores de cada ronda.
