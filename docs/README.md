# Documentación

| Documento | Para qué sirve |
|---|---|
| [MODELO.md](MODELO.md) | Cómo está montado el dato y qué reglas de cálculo sigue, con la evidencia de cada una |
| [ALTA_TORNEO.md](ALTA_TORNEO.md) | Lista de comprobación para cada torneo nuevo |
| [DECISIONES.md](DECISIONES.md) | Qué se decidió, en qué se apoya, y qué queda pendiente |
| [DIFERENCIAS.md](DIFERENCIAS.md) | Diferencias e incoherencias detectadas en el dato, sin corregir |
| [BITACORA.md](BITACORA.md) | Registro cronológico de la evolución |

## Cómo se escribe aquí

- **Sólo evidencia.** Cada afirmación va acompañada de con qué se comprobó:
  fichero, número de filas, ejemplo concreto. Lo que no se ha podido verificar se
  marca **`[NO VERIFICADO]`** y no se usa como regla.
- **Las suposiciones no se documentan como reglas.** Si el dato admite dos
  lecturas, se dicen las dos y se deja constancia de cuál se adoptó y por qué.
- **Nada en `datos/` sin OK explícito** (ver DECISIONES.md, D-001). Estos
  documentos describen el dato; no lo modifican.
