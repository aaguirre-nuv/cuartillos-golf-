# Rediseño de la sección CSC

**Abierto el 2026-10-26.** Decisiones tomadas con Álvaro y el plan para ejecutarlas. Lo que está
hecho se va anotando en [`ESTADO.md`](ESTADO.md); este documento es el destino, no la bitácora.

---

## Por qué

No es una cuestión de gusto. Esta temporada ha dejado siete fallos medidos, todos con la misma raíz:
**el dato no sabe representar la competición que realmente se juega.**

| # | Qué pasó | Raíz |
|---|---|---|
| 1 | Los cuartos hubo que colarlos en `partidos` como `ESQF`/`FSQF`. Semifinales y final no caben | **No existe el concepto de fase** |
| 2 | El rival de cuartos y los mejores segundos hubo que sacarlos de un PDF de septiembre y de un correo | **Solo se guarda nuestro grupo** |
| 3 | El `local` estaba mal en ES1 y ES5, y sigue mal en 4 de las 6 parejas de fin de semana | **Cada jornada está grabada dos veces** y las dos copias se contradicen |
| 4 | El ES2 tiene dos puntos que no se pueden atribuir; una incomparecencia era indistinguible de una derrota | **`detalle` es texto libre**, con tres convenios distintos |
| 5 | Hubo que inventar `inscripcionCerrada` en septiembre | **Una sola inscripción abierta por modalidad** |
| 6 | `calcNecesarios` está escrita **ocho veces** idénticas | Arrastre |
| 7 | Marcos, Nico y Jaime pueden apuntarse sin constar en la RFGM | **No hay forma de marcar «pendiente de federación»** |

Y uno que no es de modelo pero sí de la sección: **la master key de jsonbin está en claro** en
`microsite.html`, que es un fichero público. Cualquiera que lo abra puede leer **y escribir** ese bin.

## Las tres decisiones

1. **Arriba va la convocatoria.** Lo primero al abrir la sección es cuándo es el próximo, quién va y
   el botón de apuntarse. La clasificación baja y se pliega.
2. **Alcance: todo lo que se pueda traer.** El objetivo son los grupos enteros de las dos ligas y el
   cuadro de eliminatorias. **Depende de poder leer nextcaddy**, que hoy bloquea la red del entorno.
   Mientras no se pueda, se trabaja con nuestro grupo. **Esto no condiciona el diseño**: en el modelo
   de abajo, el alcance es cuántas filas hay en `encuentros`, no una estructura distinta.
3. **Se hace ya, sobre la temporada en curso.** Con el cuarto de fin de semana del 15 de noviembre
   por delante, lo que obliga a la estrategia de migración de más abajo.

## El modelo

La unidad es el **encuentro**: un día de competición entre dos clubes, con sus partidos dentro.

```jsonc
{
  "id": "ES-liga-J6",
  "fase": "liga",                    // clasificatorio | liga | cuartos | semifinal | final
  "grupo": "Grupo 3",                // null en las eliminatorias
  "jornada": 6,
  "fecha": "2026-10-01",
  "campo": "El Fresnillo",
  "vuelta": 2,                       // 1 = ida, 2 = vuelta. Es lo que fija el formato
  "equipos": [                       // orden del acta: estable, pero sin significado
    { "nombre": "Cuartillos",         "puntos": 4, "ups": 8 },
    { "nombre": "Club El Estudiante", "puntos": 2, "ups": 5 }
  ],
  "partidos": [
    {
      "orden": 1,
      "tipo": "individual",          // individual | fourball
      "lados": [
        { "equipo": 0, "jugadores": ["Carlos Maestro"] },
        { "equipo": 1, "jugadores": ["Alvaro Hernandez Ruiz"] }
      ],
      "ganador": null,               // 0 | 1 | null = empatado
      "margen": "A/S",
      "ups": 0,
      "incomparecencia": null        // 0 | 1 | null
    }
  ]
}
```

### Por qué no hay local ni visitante · medido el 2026-10-26

El modelo de arriba **no tiene `local` ni `visitante`**, y no es un olvido. Medido sobre las actas de
nextcaddy: de las **38 parejas** de 2026 con ida y vuelta identificables, el orden en que salen los dos
equipos en el título **no se invierte en ninguna**. Es un orden fijo por pareja.

Y es que **esta es la liga de clubes sin campo**: ningún club tiene campo propio, así que **nadie
juega en casa**. Cada jornada se disputa en un campo neutral que designa la federación. El reglamento
no menciona local ni visitante en ninguna regla —solo **ida y vuelta**, que es lo que fija el formato
(§5)—.

Conclusión: la etiqueta **LOCAL/VISITA del calendario informa de algo que no existe**. Los fallos del
`local` en ES1 y ES5 y en cuatro de las seis parejas de fin de semana **no eran errores de carga**:
eran el síntoma de guardar un campo sin sentido. En el modelo nuevo **desaparece**, y con él esa clase
entera de error.

Lo que esto arregla, punto por punto:

- **Una sola verdad por partido.** El G/P/E desde nuestro punto de vista y la clasificación del grupo
  **se calculan**, no se guardan. No hay dos sitios que puedan discrepar.
- **El `detalle` desaparece.** `ganador` + `margen` + `ups` por partido es lo que `detalle` intentaba
  decir en una cadena. Y con `jugadores` dentro de cada partido, atribuir resultados deja de depender
  de que dos listas vayan en el mismo orden.
- **`incomparecencia` es un campo**, no una nota al margen.
- **El formato sale del dato**, contando los partidos y sus tipos. Se acabó parsear
  `"2 fourball + 2 individuales"` con ocho copias de la misma función.

Alrededor, por liga:

```jsonc
{
  "id": "ES", "nombre": "Entre Semana", "escenario": 16, "nuestroGrupo": "Grupo 3",
  "grupos": [ { "nombre": "Grupo 3", "equipos": ["Cuartillos", "Foro 2000", "…"] } ],
  "clasificatorio": { "fecha": "…", "campo": "…", "posicion": 10, "puntos": 125, "jugadores": [] },
  "elegibles": [ { "nombre": "…", "licencia": "…", "altaRFGM": "2026-02-16" } ],
  "encuentros": [ … ]
}
```

**`altaRFGM`** es el fallo nº 7: la fecha en que se comunicó el jugador a la federación, o `null` si
no consta. El que lo tenga a `null` **se ve en la lista pero no puede apuntarse**, con el motivo
escrito. Hoy mismo afecta a tres.

## Cómo se migra sin romper la temporada

El riesgo de hacerlo en caliente es inventar dato al convertir. La regla es la de siempre:
**lo que no se sabe, se queda vacío.**

**Actualizado el 2026-10-26: ya no hay huecos.** Esto se escribió cuando la atribución
jugador-por-partido solo estaba verificada en ES6, FS5, FS6 y ESQF. Con el barrido de nextcaddy están
**los 454 partidos individuales de la temporada** con sus jugadores y su resultado, así que la
migración **no parte de `csc.json`, parte de las actas**. Hasta el ES2, que tenía dos puntos sin
dueño, queda resuelto. `csc.json` solo aporta lo que las actas no traen: elegibles con su licencia,
el clasificatorio, los nombres de campo como los escribimos nosotros y la incomparecencia del ES6.

Pasos, en este orden:

1. **Escribir el convertidor** `csc.json` → `csc2.json`, con los huecos declarados.
2. **Verificar por equivalencia**: renderizar la sección CSC con los dos ficheros y comprobar que
   clasificación, puntos de liga, ups y resultados salen **idénticos**. Es la misma técnica que se usó
   para validar las cargas de esta temporada, y el contraste bueno existe: los **13,5 partidos
   ganados** que la RFGM publicó para el desempate de los mejores segundos tienen que seguir saliendo.
3. **Reescribir la sección** con la convocatoria arriba, sobre el fichero nuevo.
4. **Cambiar el nombre** y borrar lo viejo, no antes.

`csc.json` se queda intacto hasta el paso 4, así que en cualquier momento se vuelve atrás.

## Lo que hay que decidir todavía

- **La master key de jsonbin.** En un sitio estático, cualquier credencial de escritura queda
  expuesta: no hay forma de esconderla. Las salidas reales son asumirlo, mover las inscripciones a un
  formulario externo, o poner algo delante que escriba por nosotros. Hay que elegir, no arrastrarlo.
- **El ranking de selección**, aplazado a 2027 en §15 del reglamento. Si la sección se rehace ahora,
  es el momento de decidir si cambia con ella.
- **Las dos grafías de El Encín.** `campos.json` y el calendario escriben `El Encin`; `csc.json`,
  `El Encín` y `El Encín Golf`. No rompe nada hoy porque el campo del CSC es solo una etiqueta, pero
  si alguna vez se cruzan las dos competiciones hay que unificarlo.
