# Fuentes de datos de la RFEG · hándicap y vueltas de los socios

**Medido el 2026-10-20.** Exploración para el frente nuevo de **evolución semanal de forma y hándicap
de cada jugador**, pensado como ayuda para seleccionar a quién llevar a la CSC (ver
[`reglamento-csc-2026.md`](reglamento-csc-2026.md) §15, donde quedó apuntado separar **forma** e
**implicación** para 2027). Todavía no hay diseño aprobado: esto es solo qué fuentes hay y qué dan.

## Lo que había · dos flujos de Power Automate Desktop, abandonados

Álvaro tenía dos flujos de PAD que recorrían las licencias de `Jugadores.xlsx` y volcaban a Excel.
El texto de los flujos se pegó en `docs/Untitled-1.txt` y `docs/Untitled-2.txt` (2 y 4 MB, con
capturas de pantalla de los controles y el usuario de la web; **no se suben al repo**). Las salidas
viven en OneDrive, `Golf\Cuartillos\Comité Dirección\Jugadores\`:

| Flujo | Página | Salida | Última ejecución |
|---|---|---|---|
| Todas las vueltas («FichaJugador») | `http://82.223.130.155:6050/Ficha_Actividad.aspx` → `Ficha_Actividad_Results.aspx?sLic=<licencia>&sNom=` | `Vueltas.xlsx`, ~3.300 filas, formato EGA antiguo (HCP inicial, de juego y final por vuelta), licencia en la columna 15 | 2024-03-16 |
| Últimas 20 · hándicap mundial («HandicapMundial») | `http://82.223.130.155:6050/handicap.aspx`, botón «Consultar Hcp Mundial» → `handicap_resul_mundial.aspx?sLic=<licencia>` | Carpeta `HandicapMundial\`: `HandicapMundial.xlsx` (20 últimas), `Diferenciales.xlsx`, `NivelJuego.xlsx`, `Ajustes.xlsx`, `RBA.xlsx` y `Handicap actual.xlsx` (histórico de hándicap por fecha desde 2025-02-09) | 2025-11-23 |

El segundo flujo llegaba a `handicap.aspx` desde la web antigua de la RFEG: `rfegolf.es` →
Servicios → **Área del Jugador**. Ese camino antiguo ya no existe: `PaginasServicios/areadeljugador.aspx`
redirige a la portada nueva.

## Lo que hay hoy · medido el 2026-10-20

### Servidor antiguo `82.223.130.155:6050` («Área del Jugador», ASP.NET 2.0)

Sigue en pie, por HTTP y sin dominio. Muestra los errores completos del servidor.

| Página | Resultado | Qué significa |
|---|---|---|
| `handicap.aspx` → «Consultar» → `handicap_resul.aspx?sLic=` | **200, funciona sin sesión** | Nombre, licencia, hándicap exacto, fecha de última modificación y estado. Probado con `CME6628917` (Álvaro): **7.3, modificado el 13/9/2026**, que cuadra con el buscador nuevo |
| `handicap.aspx` → «Consultar Hcp Mundial» → `handicap_resul_mundial.aspx?sLic=` | **500, error de compilación del servidor** (`handicap_resul_mundial` no concuerda con su `inherits`) | Es la página de las 20 últimas vueltas. **Está rota en su lado**, no por cómo se pregunta |
| `Ficha_Actividad.aspx` y `Ficha_Actividad_Results.aspx` | **500**, `InvalidCastException` convirtiendo `""` a `Long` en `LicenciaUsuario(idCliente)` | Pide el identificador del **usuario con sesión iniciada**, que no hay. El flujo arrancaba con usuario `aaguirre` y no borraba cookies: **hipótesis** de que funcionaba con la sesión abierta en el navegador |

**Riesgo:** es una aplicación antigua, publicada por IP, con una página ya rota. No hay que construir
nada que dependa de ella sin contar con que desaparezca.

### Web nueva `rfegolf.es` · buscador público de hándicap

La página `https://rfegolf.es/aprende-mejora/consulta-handicap` usa por debajo una API **pública y sin
sesión**:

```
GET https://rfegolf.es/wp-json/handicap-search/v1/search?q=<licencia o nombre>&size=<n>
```

Configuración de la página: mínimo 5 caracteres, máximo 20 resultados. Devuelve JSON con, por
jugador: `guid_licence`, `full_name`, `competition_name`, `club_title`, `federation_title`,
**`handicap`**, **`date_hdc_updated_at`**, `level_code`, `enum_gender`, `is_professional`, `id_ref`.

- **Da el hándicap actual y la fecha de su último cambio, no las vueltas.**
- **Busca por nombre o licencia, no por club**: `q=CUARTILLOS` devolvió 2 jugadores de otros clubes
  cuyo nombre casaba. **Y aunque buscara por club no serviría**: no todos los socios tienen la licencia
  por Cuartillos (Álvaro, 2026-10-20). La lista sale de nuestro maestro, por licencia.

### `app.rfegolf.es` · «MIGOLF», con sesión

Según el texto de la propia página de consulta, con sesión se ve el **historial de las últimas vueltas,
el promedio de las mejores y la evolución**, de **los datos de uno mismo**. **No medido**: si desde ahí
se pueden ver las vueltas de otro jugador. El inicio de sesión lo tendría que hacer Álvaro.

## Lo que queda abierto

- **H1 · EN VALIDACIÓN.** No hay hoy una fuente **pública** de las **vueltas** de otros jugadores: la del
  servidor antiguo está rota y la web nueva sin sesión solo da el hándicap. **Álvaro, 2026-10-20:** *«he
  visto y extraído las vueltas de todos… sin problema»*. **Sin medir** si fue desde MIGOLF
  (`app.rfegolf.es`) o con los flujos antiguos. **Lo primero al retomar:** que Álvaro inicie sesión en
  MIGOLF en el navegador compartido y mirar cómo se llega a las vueltas de otra licencia, y si hay una
  API por debajo como en el buscador público.
- Con lo medido sí es posible, sin sesión, una **foto semanal del hándicap** de cada socio desde el
  buscador nuevo, enlazada con el histórico que ya hay (`datos/handicaps.json` desde 2018 y
  `Handicap actual.xlsx` desde 2025-02).
