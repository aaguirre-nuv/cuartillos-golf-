# Bitácora

Registro cronológico, de lo más reciente a lo más antiguo. Sirve para ver la
evolución: qué se analizó, qué se decidió, qué se cambió y qué se deshizo.

Cada entrada dice **qué se hizo** y **qué quedó en el dato**. Si un cambio se
revirtió, se deja constancia en lugar de borrar la entrada.

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

**Abierto al cerrar la entrada:** P-001 (orden del countback contra el
reglamento), P-002 (temporada de alta de Nicolás y Marcos), P-003 (su equipo),
P-004 (dónde se declara el socio de 2026), P-005 (las correcciones).

### Hallazgos que conviene no perder de vista

- **El modelo actual no puede recalcular el desempate.** Los segmentos de 9, 6 y
  3 hoyos no existen como campo, y en torneos a doble vuelta `handicapJuego`
  guarda sólo el de la última ronda, no la suma que usa el desempate.
- **2026 T6 Layos** reparte 500 y 300 puntos entre dos jugadores empatados a
  neto, handicap de juego y últimos 9 hoyos, y el que gana el resto del countback
  figura segundo. Es la diferencia de mayor peso encontrada.
- **Asignar equipo a un jugador incorporado cambia clasificaciones por equipos ya
  publicadas**, porque el `teamScore` sale de los 2 mejores de cada ronda.
