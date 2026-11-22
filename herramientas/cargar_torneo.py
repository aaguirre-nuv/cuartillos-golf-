"""Carga un torneo del circuito interno desde los tres Excel de golfdirecto.

Uso (desde la raiz del repo):

    python herramientas/cargar_torneo.py --temp 2026 --torneo 9 --carpeta "%USERPROFILE%\\Downloads"
    python herramientas/cargar_torneo.py --temp 2026 --torneo 9 --carpeta ... --aplicar

Sin --aplicar solo simula: comprueba, calcula y ensena el resultado sin escribir nada.

Entradas (en --carpeta, se coge el mas reciente de cada uno):
  * ``... TORNEO <n> - Jugadores*.xlsx``           tarjeta hoyo a hoyo (bruto), licencia, equipo
  * ``... TORNEO <n> - Resultados HANDICAP.xlsx``  HCPE, HCPG, Estado, neto por hoyo
  * ``... TORNEO <n> - Resultados SCRATCH.xlsx``   bruto respecto al par por hoyo (de ahi el par)

Salidas: ``tarjetas_<t>.json``, ``clasificacion_<t>.json``, ``clas_matrix_<t>.json``,
``equipos_clasificacion_<t>.json``, ``jugado`` en ``calendario.json`` y ``CV`` en ``microsite.html``.

Reglas que aplica, cada una con su documento:
  * Desempate RFEG: neto, hcp de juego, netos ultimos 9-12-15-16-17 (docs/desempates.md).
  * Escala de puntos por tipo de torneo (docs/incorporacion-de-socios.md).
  * Equipos: 2 mejores difNeto, 10 de asistencia por presentado, desempate por hcp de juego
    sumado (docs/clasificacion-por-equipos.md).
  * Invitados: como Javier Aguirre en 2026:3 -> rk 0, pts 0, ``tipoParticipacion: Inv``, fuera de
    la general y de equipos, pero ocupan ``posicionTorneo``.
  * No clasificados (tarjeta incompleta o no entregada, ``Estado`` distinto de ``active`` o
    ``--no-clasificado``): sin tarjeta en ``tarjetas_<t>.json`` (el microsite ordena por neto y la
    pondria la primera), fila en ``clasificacion`` con ``noClasificado: true`` y sin puesto ni
    puntos, y cuentan para la asistencia de su equipo (decision de Alvaro del 2026-11-22).
  * Equipo con un solo resultado: ``valid: false`` y por detras de los validos, como en 2026:2 y
    2026:4 (en 2026:6 se hizo al reves; criterio revisable, ver docs/clasificacion-por-equipos.md).

Antes de calcular, recalcula lo ya publicado con las mismas reglas y para si no cuadra: asi un
cambio de formato o de regla no pasa desapercibido.
"""
import argparse, glob, json, os, re, sys, unicodedata

import openpyxl

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(REPO, 'datos')

ESCALA = {
    2: [500, 300, 190, 135, 110, 100, 90, 85, 80, 75, 70, 65, 60, 57, 55, 53, 51, 49, 47, 45, 44, 43],
    3: [600, 330, 210, 150, 120, 110, 100, 94, 88, 82, 77, 72, 68, 64, 61, 59, 57, 55, 53, 51, 50, 49],
}
PUNTOS_EQUIPO = [500, 400, 300, 200, 175, 150, 125, 100, 75]
ASISTENCIA = 10
CATEGORIA = {-1: 'birdie', 0: 'par', 1: 'bogey', 2: 'dbogey'}


def categoria(dif):
    if dif <= -2:
        return 'eagle'
    if dif >= 3:
        return 'tbogey'
    return CATEGORIA[dif]


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'\s+', ' ', s).strip().upper()


def leer_json(nombre):
    with open(os.path.join(DATOS, nombre), encoding='utf-8') as f:
        return json.load(f)


def volcar(obj):
    return json.dumps(obj, ensure_ascii=False)


def escribir_json(nombre, obj, original):
    """Escribe con el mismo formato que el fichero original (una linea, mismo final)."""
    ruta = os.path.join(DATOS, nombre)
    texto = volcar(obj)
    if original.endswith('\n'):
        texto += '\n'
    texto.encode('utf-8')  # valida antes de abrir en escritura (trampa de io.open)
    tmp = ruta + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='') as f:
        f.write(texto)
    os.replace(tmp, ruta)


def leer_crudo(nombre):
    with open(os.path.join(DATOS, nombre), encoding='utf-8', newline='') as f:
        return f.read()


def excel(carpeta, torneo, patron):
    fs = glob.glob(os.path.join(carpeta, f'*TORNEO {torneo} - {patron}*.xlsx'))
    if not fs:
        sys.exit(f'No encuentro el Excel «{patron}» del torneo {torneo} en {carpeta}')
    f = max(fs, key=os.path.getmtime)
    ws = openpyxl.load_workbook(f, read_only=True, data_only=True).worksheets[0]
    filas = list(ws.iter_rows(values_only=True))
    cab = [str(c).strip() if c is not None else None for c in filas[0]]
    datos = [dict(zip(cab, r)) for r in filas[1:] if r and r[0] is not None]
    print(f'  {os.path.basename(f)}: {len(datos)} filas')
    return datos


def lic(x):
    return str(x or '').strip().upper()


# ---------------------------------------------------------------- derivados de una tarjeta

def derivar(hoyos, par_total):
    """Campos de tarjeta que salen del objeto hoyos. Devuelve dict."""
    ks = [str(i) for i in range(1, 19)]
    b = {k: hoyos[k]['b'] for k in ks}
    n = {k: hoyos[k]['n'] for k in ks}
    p = {k: hoyos[k]['p'] for k in ks}
    ida = sum(b[k] for k in ks[:9]); vta = sum(b[k] for k in ks[9:])
    pi = sum(p[k] for k in ks[:9]); pv = sum(p[k] for k in ks[9:])
    ni = sum(n[k] for k in ks[:9]); nv = sum(n[k] for k in ks[9:])
    cnt = {c: 0 for c in ('eagle', 'birdie', 'par', 'bogey', 'dbogey', 'tbogey')}
    for k in ks:
        cnt[categoria(b[k] - p[k])] += 1
    pp = {3: 0, 4: 0, 5: 0}
    for k in ks:
        pp[p[k]] = pp.get(p[k], 0) + b[k] - p[k]
    return dict(ida=ida, vta=vta, total=ida + vta, netoIda=ni, netoVta=nv, netoTotal=ni + nv,
                parIda=pi, parVta=pv, difPar=ida + vta - par_total, difIda=ida - pi, difVta=vta - pv,
                **cnt, p3=pp[3], p4=pp[4], p5=pp[5], difNetoIda=ni - pi, difNetoVta=nv - pv)


def clave_desempate(neto, hcpj, netos_hoyo):
    tramo = lambda desde: sum(netos_hoyo[i] for i in range(desde, 19))
    return (neto, hcpj, tramo(10), tramo(7), tramo(4), tramo(3), tramo(2))


# ---------------------------------------------------------------- temporada

def recalcular_matriz(matriz, n_torn_punt):
    for r in matriz:
        r['nJugados'] = len(r['torneos'])
        r['nPunt'] = min(n_torn_punt, r['nJugados'])
        orden = sorted(r['torneos'], key=lambda t: -r['torneos'][t])
        r['computan'] = orden[:r['nPunt']]
        r['total'] = sum(r['torneos'][t] for t in r['computan'])
    matriz.sort(key=lambda r: -r['total'])  # estable: los empatados conservan su orden
    for i, r in enumerate(matriz, 1):
        r['rk'] = i


def recalcular_equipos(equipos, n_torn_punt):
    for e in equipos:
        e['nJugados'] = len(e['torneos'])
        e['nPunt'] = min(n_torn_punt, e['nJugados'])
        orden = sorted(e['torneos'], key=lambda t: -e['torneos'][t])
        e['computan'] = orden[:e['nPunt']]
        e['total'] = sum(e['torneos'][t] for t in e['computan'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--temp', type=int, required=True)
    ap.add_argument('--torneo', type=int, required=True)
    ap.add_argument('--carpeta', required=True)
    ap.add_argument('--no-clasificado', action='append', default=[], help='licencia')
    ap.add_argument('--aplicar', action='store_true')
    a = ap.parse_args()
    T, N = a.temp, a.torneo
    tid = f'{T}:{N}'

    crudo = {f: leer_crudo(f) for f in (f'tarjetas_{T}.json', f'clasificacion_{T}.json',
                                         f'clas_matrix_{T}.json', f'equipos_clasificacion_{T}.json',
                                         'calendario.json')}
    tarjetas = json.loads(crudo[f'tarjetas_{T}.json'])
    clasif = json.loads(crudo[f'clasificacion_{T}.json'])
    matriz = json.loads(crudo[f'clas_matrix_{T}.json'])
    eqc = json.loads(crudo[f'equipos_clasificacion_{T}.json'])
    cal = json.loads(crudo['calendario.json'])
    maestro = [x for x in leer_json('jugadores.json') if x.get('temporada') == T]

    # ---- 0. el formato se conserva y lo publicado se reproduce con estas reglas
    for f, obj in (('tarjetas', tarjetas), ('clasificacion', clasif), ('matriz', matriz), ('equipos', eqc), ('calendario', cal)):
        nombre = {'matriz': f'clas_matrix_{T}.json', 'equipos': f'equipos_clasificacion_{T}.json',
                  'calendario': 'calendario.json'}.get(f, f'{f}_{T}.json')
        if volcar(obj) != crudo[nombre].rstrip('\n'):
            sys.exit(f'FORMATO: volcar {nombre} no da los mismos bytes; no se escribe nada')
    errores = []
    for t in tarjetas:
        if not t.get('hoyos') or len(t['hoyos']) != 18 or t.get('ronda'):
            continue
        d = derivar(t['hoyos'], t['parTotal'])
        for k, v in d.items():
            if k in t and t[k] != v:
                errores.append(f"{t['ntorn']} {t['nombre']} {k}: dato {t[k]} calculado {v}")
    if errores:
        # Conocido (2026-11-22): de 2026:3 a 2026:8 p3/p4/p5 guardan cuantos hoyos hay de cada par en vez
        # de los golpes sobre el par, que es lo que son en 2021-2026:2 y lo que pinta el microsite.
        otros = [e for e in errores if not re.search(r' p[345]: ', e)]
        print(f'  AVISO: {len(errores)} campos de tarjetas ya publicadas no cuadran con sus hoyos (no se tocan); '
              f'{len(errores) - len(otros)} son p3/p4/p5')
        for e in otros[:15]:
            print('   ', e)
    jugados = [c for c in cal if c['temporada'] == T and c.get('jugado') == 1]
    ntp_actual = max(jugados, key=lambda c: c['nTorneo'])['nTornPunt']
    m2 = json.loads(volcar(matriz)); recalcular_matriz(m2, ntp_actual)
    e2 = json.loads(volcar(eqc['equipos'])); recalcular_equipos(e2, ntp_actual)
    dm = [(r['jugador'], r['total'], s['total']) for r, s in zip(matriz, m2) if r['jugador'] != s['jugador'] or r['total'] != s['total']]
    de = [(x['nombre'], x['total'], y['total']) for x, y in zip(eqc['equipos'], e2) if x['total'] != y['total']]
    if dm or de:
        sys.exit(f'REGRESION: la general o los equipos publicados no se reproducen: {dm[:5]} {de[:5]}')
    print(f'  Reproducidas la general ({len(matriz)} jugadores) y la de equipos con nTornPunt {ntp_actual}')

    if any(t['ntorn'] == N for t in tarjetas) or any(c['idTorneo'] == tid for c in clasif):
        sys.exit(f'El torneo {tid} ya esta cargado')
    torneo = next(c for c in cal if c['id'] == tid)
    campo, fecha, par_total = torneo['campo'], torneo['fecha'], torneo['parTotal']
    escala, ntp = ESCALA[torneo['tipoTorneo']], torneo['nTornPunt']
    print(f'Torneo {tid}: {campo} {fecha}, par {par_total}, tipo {torneo["tipoTorneo"]}, cuentan {ntp}')

    # ---- 1. Excel
    jug = excel(a.carpeta, N, 'Jugadores')
    hcp = {lic(x['Licencia']): x for x in excel(a.carpeta, N, 'Resultados HANDICAP')}
    scr = {lic(x['Licencia']): x for x in excel(a.carpeta, N, 'Resultados SCRATCH')}
    if set(hcp) != set(scr):
        sys.exit(f'HANDICAP y SCRATCH no traen a los mismos: {set(hcp) ^ set(scr)}')

    por_lic = {lic(x['licencia']): x for x in maestro}
    por_nom = {norm(x['nombreCompleto']): x for x in maestro if x.get('nombreCompleto')}
    nombres_eq = {e['idTempEquipo']: e for e in eqc['equipos']}

    filas, sin_tarjeta, avisos = [], [], []
    for x in jug:
        L = lic(x['Licencia'])
        nom_xl = f"{x['Nombre']} {x['Apellidos']}"
        m = por_lic.get(L) or por_nom.get(norm(nom_xl))
        if not m:
            sys.exit(f'{nom_xl} ({L}) no esta en el maestro de {T}: darlo de alta antes')
        if lic(m['licencia']) != L:
            avisos.append(f"{m['nombre']}: licencia {L} en el Excel y {m['licencia']} en el maestro (casado por nombre)")
        if L not in hcp:
            sin_tarjeta.append(m['nombre'])
            continue
        h, s = hcp[L], scr[L]
        if m['tipoParticipacion'] == 'Si' and x.get('Equipo (num)') != m.get('equipo'):
            avisos.append(f"{m['nombre']}: equipo {x.get('Equipo (num)')} en el Excel y {m.get('equipo')} en el maestro (manda el maestro)")
        nc = h['Estado'] != 'active' or L in [lic(v) for v in a.no_clasificado]
        jugados = h.get('Jugados')
        hoyos = {}
        for i in range(1, 19):
            b = x.get(f'h{i}')
            if b is None:
                continue
            p = b - s[f'Res. {i}']
            hoyos[str(i)] = {'b': b, 'n': h[f'Neto {i}'], 'p': p, 'c': categoria(b - p)}
        filas.append(dict(m=m, lic=L, h=h, s=s, hoyos=hoyos, nc=nc, jugados=jugados,
                          inv=m['tipoParticipacion'] != 'Si'))

    # par por hoyo: el mismo para todos
    pares = {}
    for f in filas:
        for k, v in f['hoyos'].items():
            pares.setdefault(k, set()).add(v['p'])
    malos = {k: v for k, v in pares.items() if len(v) != 1}
    if malos or sum(next(iter(pares[str(i)])) for i in range(1, 19)) != par_total:
        sys.exit(f'El par por hoyo no cuadra con el calendario ({par_total}): {malos or pares}')

    clas = [f for f in filas if not f['nc']]
    for f in clas:
        if len(f['hoyos']) != 18:
            sys.exit(f"{f['m']['nombre']} tiene {len(f['hoyos'])} hoyos y figura como clasificado")
        d = derivar(f['hoyos'], par_total)
        if d['total'] != f['s']['Bruto Total'] or d['netoTotal'] != f['h']['Neto Total']:
            sys.exit(f"{f['m']['nombre']}: bruto {d['total']}/{f['s']['Bruto Total']} neto {d['netoTotal']}/{f['h']['Neto Total']}")
        f['d'] = d
        f['clave'] = clave_desempate(d['netoTotal'], f['h']['HCPG'], {int(k): v['n'] for k, v in f['hoyos'].items()})
    clas.sort(key=lambda f: f['clave'])
    for a_, b_ in zip(clas, clas[1:]):
        if a_['clave'] == b_['clave']:
            sys.exit(f"Empate total entre {a_['m']['nombre']} y {b_['m']['nombre']}: sorteo, preguntar")

    # contraste con el orden del Excel de handicap
    orden_xl = [f['m']['nombre'] for f in sorted(clas, key=lambda f: f['h']['Pos'])]
    orden_yo = [f['m']['nombre'] for f in clas]
    print('  Orden del Excel de handicap ' + ('IGUAL' if orden_xl == orden_yo else 'DISTINTO') + ' al del criterio RFEG')
    if orden_xl != orden_yo:
        for i, (x, y) in enumerate(zip(orden_xl, orden_yo), 1):
            if x != y:
                print(f'    {i}: Excel {x} / RFEG {y}')

    # ---- 2. puestos y puntos
    rs = 0
    for pos, f in enumerate(clas, 1):
        f['pos'] = pos
        if f['inv']:
            f['rkS'], f['pts'] = 0, 0
        else:
            rs += 1
            f['rkS'], f['pts'] = rs, escala[rs - 1]

    # ---- 3. tarjetas
    nuevas_t = []
    for f in clas:
        m, d = f['m'], f['d']
        t = {'temp': T, 'ntorn': N, 'nombre': m['nombre'], 'licencia': f['lic'], 'campo': campo, 'fecha': fecha,
             'hcp': f['h']['HCPE'], 'hcpJ': f['h']['HCPG'], 'parTotal': par_total}
        for k in ('ida', 'vta', 'total', 'netoIda', 'netoVta', 'netoTotal', 'parIda', 'parVta', 'difPar', 'difIda',
                  'difVta', 'eagle', 'birdie', 'par', 'bogey', 'dbogey', 'tbogey', 'p3', 'p4', 'p5'):
            t[k] = d[k]
        t['rk'], t['pts'] = f['rkS'], f['pts']
        t['equipo'] = m.get('equipo') if not f['inv'] else None
        t['nombreEq'] = m.get('nombreEquipo') if not f['inv'] else None
        t['hoyos'] = f['hoyos']
        t['difNetoIda'], t['difNetoVta'], t['invitado'] = d['difNetoIda'], d['difNetoVta'], f['inv']
        nuevas_t.append(t)

    # ---- 4. clasificacion
    nuevas_c = []
    for f in clas + [f for f in filas if f['nc']]:
        m = f['m']
        d = f.get('d')
        c = {'id': f"{tid}:{m['nombre']}", 'temporada': T, 'idTorneo': tid, 'fecha': fecha, 'campo': campo,
             'idTempJugador': m['idTempJugador'], 'licencia': f['lic'], 'handicapReal': f['h']['HCPE'],
             'handicapJuego': f['h']['HCPG'], 'par': par_total,
             'bruto': d['total'] if d else None, 'neto': d['netoTotal'] if d else None,
             'difBruto': d['difPar'] if d else None, 'difNeto': d['netoTotal'] - par_total if d else None,
             'posicionTorneo': f.get('pos'), 'rankingSocios': f.get('rkS', 0), 'puntos': f.get('pts', 0),
             'idTempEquipo': m.get('idTempEquipo') if not f['inv'] else None,
             'tipoParticipacion': m['tipoParticipacion']}
        if f['nc']:
            c['noClasificado'] = True
            c['hoyosJugados'] = len(f['hoyos'])
        nuevas_c.append(c)

    # ---- 5. equipos
    nuevas_e = []
    for e in eqc['equipos']:
        js = [f for f in filas if not f['inv'] and f['m'].get('idTempEquipo') == e['idTempEquipo']]
        val = sorted([f for f in js if not f['nc']], key=lambda f: f['clave'])
        dif = lambda f: f['d']['netoTotal'] - par_total
        top = val[:2]
        ts = sum(dif(f) for f in top) if top else None
        jl = [{'nombre': f['m']['nombre'], 'difNeto': dif(f), 'neto': f['d']['netoTotal'], 'computa': f in top} for f in val]
        jl += [{'nombre': f['m']['nombre'], 'difNeto': None, 'neto': None, 'computa': False, 'noClasificado': True}
               for f in js if f['nc']]
        nuevas_e.append({'idTempEquipo': e['idTempEquipo'], 'temporada': T, 'idTorneo': tid, 'teamScore': ts,
                         'teamScoreStr': '-' if ts is None else (f'+{ts}' if ts > 0 else str(ts)),
                         'valid': len(val) >= 2, 'ranking': None, 'nJugadores': len(js),
                         'puntosEquipos': None, 'puntosAsistencia': ASISTENCIA * len(js), 'puntosTotales': None,
                         'jugadores': jl, '_hcp': sum(f['h']['HCPG'] for f in top)})
    nuevas_e.sort(key=lambda r: (0 if r['valid'] else 1 if r['teamScore'] is not None else 2,
                                 r['teamScore'] if r['teamScore'] is not None else 0, r['_hcp']))
    for i, r in enumerate(nuevas_e):
        if i and (r['valid'], r['teamScore'], r['_hcp']) == (nuevas_e[i-1]['valid'], nuevas_e[i-1]['teamScore'], nuevas_e[i-1]['_hcp']) and r['teamScore'] is not None:
            avisos.append(f"Equipos empatados tambien en hcp: {r['idTempEquipo']} y {nuevas_e[i-1]['idTempEquipo']} (falta mirar hoyos)")
        r['ranking'] = i + 1
        r['puntosEquipos'] = PUNTOS_EQUIPO[i]
        r['puntosTotales'] = r['puntosEquipos'] + r['puntosAsistencia']
    for r in nuevas_e:
        del r['_hcp']

    # ---- 6. temporada
    por_jug = {r['jugador']: r for r in matriz}
    for f in clas:
        if f['inv']:
            continue
        nom = f['m']['nombre']
        if nom not in por_jug:
            r = {'temp': T, 'jugador': nom, 'total': 0, 'torneos': {}, 'computan': [], 'nPunt': 0, 'nJugados': 0,
                 'sinEquipo': False, 'rk': 0}
            matriz.append(r); por_jug[nom] = r
            avisos.append(f'{nom} entra nuevo en la general')
        por_jug[nom]['torneos'][tid] = f['pts']
    recalcular_matriz(matriz, ntp)
    for r in nuevas_e:
        nombres_eq[r['idTempEquipo']]['torneos'][tid] = r['puntosTotales']
    recalcular_equipos(eqc['equipos'], ntp)

    # ---- informe
    print(f'\nSin tarjeta (baja): {sin_tarjeta or "nadie"}')
    for v in avisos:
        print('AVISO:', v)
    print(f'\n{"pos":>3} {"rkS":>3} {"pts":>4}  {"jugador":<32} neto hcpJ  equipo')
    for f in clas:
        print(f"{f['pos']:>3} {f['rkS']:>3} {f['pts']:>4}  {f['m']['nombre']:<32} {f['d']['netoTotal']:>4} {f['h']['HCPG']:>4}  "
              f"{'invitado' if f['inv'] else f['m'].get('nombreEquipo')}")
    for f in filas:
        if f['nc']:
            print(f"  -   -    -  {f['m']['nombre']:<32} no clasificado ({len(f['hoyos'])} hoyos, {f['h']['Estado']})  {f['m'].get('nombreEquipo')}")
    print('\nEquipos:')
    for r in nuevas_e:
        print(f"  {r['ranking']} {r['idTempEquipo'][5:]:<30} {r['teamScoreStr']:>4} {'valido' if r['valid'] else 'NO valido':<9} "
              f"n={r['nJugadores']} {r['puntosEquipos']}+{r['puntosAsistencia']}={r['puntosTotales']}  "
              + ', '.join(f"{j['nombre']} {j['difNeto'] if j['difNeto'] is not None else 'NC'}{'*' if j['computa'] else ''}" for j in r['jugadores']))
    print('\nGeneral (10 primeros):')
    for r in matriz[:10]:
        print(f"  {r['rk']:>2} {r['jugador']:<32} {r['total']:>5}  (T{N}: {r['torneos'].get(tid, '-')})")
    print('\nEquipos temporada:')
    for e in sorted(eqc['equipos'], key=lambda e: -e['total']):
        print(f"  {e['nombre']:<32} {e['total']:>5}  (T{N}: {e['torneos'].get(tid)})")

    if not a.aplicar:
        print('\nSIMULACION: no se ha escrito nada. Repetir con --aplicar.')
        return

    tarjetas.extend(nuevas_t)
    clasif.extend(nuevas_c)
    eqc['clasificacion'].extend(nuevas_e)
    torneo['jugado'] = 1
    for nombre, obj in ((f'tarjetas_{T}.json', tarjetas), (f'clasificacion_{T}.json', clasif),
                        (f'clas_matrix_{T}.json', matriz), (f'equipos_clasificacion_{T}.json', eqc),
                        ('calendario.json', cal)):
        escribir_json(nombre, obj, crudo[nombre])
    ruta_html = os.path.join(REPO, 'microsite.html')
    with open(ruta_html, encoding='utf-8', newline='') as f:
        html = f.read()
    cv_viejo = re.search(r"var CV='\?v=([^']+)'", html).group(1)
    base = re.sub(r'\D', '', fecha_hoy := __import__('datetime').date.today().isoformat())
    cv_nuevo = base if cv_viejo[:8] != base else base + chr(ord(cv_viejo[8]) + 1 if len(cv_viejo) > 8 else ord('a'))
    html = html.replace(f"var CV='?v={cv_viejo}'", f"var CV='?v={cv_nuevo}'", 1)
    with open(ruta_html, 'w', encoding='utf-8', newline='') as f:
        f.write(html)
    print(f'\nEscrito. CV {cv_viejo} -> {cv_nuevo}')


if __name__ == '__main__':
    main()
