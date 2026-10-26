"""Convierte la temporada 2026 al modelo nuevo: docs/fuentes/nextcaddy-2026.json -> datos/csc2.json

La materia prima son las actas federativas, no csc.json. De csc.json solo se
toma lo que las actas no traen: elegibles con licencia, el clasificatorio, los
nombres de campo como los escribimos nosotros, y la incomparecencia del ES6.

No se escribe `local` ni `visitante`: en la liga de clubes sin campo nadie
juega en casa, y el orden del titulo del acta no alterna entre ida y vuelta en
ninguna de las 38 parejas medidas. Lo que manda es `vuelta` (1 o 2), que es lo
que fija el formato segun el 5 del reglamento.
"""
import json
import re
import sys
import unicodedata
from collections import defaultdict

FUENTE, VIEJO, SALIDA = sys.argv[1], sys.argv[2], sys.argv[3]

POSTERIORES = {'Jaime Villanueva', 'Marcos Ruiz', 'Nicolas Sequera'}

# --- nombres de club -------------------------------------------------------
# Las actas escriben 24 clubes de 81 formas distintas: la tabla esta en
# herramientas/clubes.py, y alli se comprueba que los grupos salen 4 de 4 en
# entre semana y 5 de 4 en fin de semana, como dice el reglamento.
sys.path.insert(0, 'herramientas')
from clubes import club, pelado  # noqa: E402

# --- jugadores nuestros ----------------------------------------------------
J = json.load(open('datos/jugadores.json', encoding='utf-8'))
CANON = {}
for r in J:
    CANON[pelado(r['nombre'])] = r['nombre']
    if r.get('nombreCompleto'):
        CANON[pelado(r['nombreCompleto'])] = r['nombre']


def jugador(n, es_nuestro):
    return CANON.get(pelado(n), n) if es_nuestro else n


# --- conversion ------------------------------------------------------------
E = json.load(open(FUENTE, encoding='utf-8'))
V = json.load(open(VIEJO, encoding='utf-8'))
viejo = {m['id']: m for m in V['modalidades']}

# jornada y vuelta: por pareja, ordenando por fecha
porliga = defaultdict(list)
for e in E:
    porliga[e['liga']].append(e)
fechas = {l: sorted({x['fecha'] for x in v if x['fase'] == 'liga' and x['fecha']})
          for l, v in porliga.items()}

# Nextcaddy escribe los campos con su nombre largo ("Layos Casa Campo S A").
# Donde tenemos el nuestro, manda el nuestro.
campo_nuestro = {(m['id'], p['fecha']): p['campo']
                 for m in V['modalidades'] for p in m['partidos']}

ligas = []
for lid in ('ES', 'FS'):
    vj = viejo[lid]
    encs = []
    pares = defaultdict(list)
    for e in sorted(porliga[lid], key=lambda x: (x['fecha'] or '', x['id'])):
        if e['fase'] == 'liga':
            pares[tuple(sorted(club(q['nombre']) for q in e['equipos']))].append(e)
    orden_pareja = {id(e): i + 1 for v in pares.values() for i, e in enumerate(v)}

    # Los grupos salen de quien juega contra quien. Solo conocemos el numero
    # federativo del nuestro; los demas van sin nombre, pero con id propio para
    # poder calcular su clasificacion.
    ady = defaultdict(set)
    for a, b in pares: ady[a].add(b); ady[b].add(a)
    comps, vistos = [], set()
    for t in sorted(ady):
        if t in vistos: continue
        comp, cola = set(), [t]
        while cola:
            n = cola.pop()
            if n in comp: continue
            comp.add(n); cola += [m for m in ady[n] if m not in comp]
        comps.append(sorted(comp)); vistos |= comp
    grupos, de_equipo = [], {}
    for i, c in enumerate(sorted(comps), 1):
        gid = f'{lid}-g{i}'
        nuestro_g = 'Cuartillos' in c
        grupos.append({'id': gid, 'nombre': vj['grupo'] if nuestro_g else None,
                       'nuestro': nuestro_g, 'equipos': c})
        for t in c: de_equipo[t] = gid

    for e in sorted(porliga[lid], key=lambda x: (x['fecha'] or '9999', x['id'])):
        if not e['partidos']:
            continue
        eqs = [club(q['nombre']) for q in e['equipos']]
        nuestro = [i for i, n in enumerate(eqs) if n == 'Cuartillos']
        enc = {
            'id': f"{lid}-{e['fase']}-{e['fecha']}",
            'fase': e['fase'],
            'grupo': de_equipo.get(eqs[0]) if e['fase'] == 'liga' else None,
            'jornada': fechas[lid].index(e['fecha']) + 1 if e['fase'] == 'liga' and e['fecha'] in fechas[lid] else None,
            'vuelta': orden_pareja.get(id(e)),
            'fecha': e['fecha'],
            'campo': campo_nuestro.get((lid, e['fecha']), e['campo']),
            'equipos': [{'nombre': eqs[i], 'puntos': q['puntos'], 'ups': q['ups']}
                        for i, q in enumerate(e['equipos'])],
            'partidos': [],
        }
        for pa in e['partidos']:
            lados, ganador = [], None
            for s in pa['lados']:
                i = eqs.index(club(s['equipo']))
                if s.get('gana'):
                    ganador = i
                lados.append({'equipo': i,
                              'jugadores': [jugador(j, i in nuestro) for j in s['jugadores']]})
            lados.sort(key=lambda x: x['equipo'])
            m = re.match(r'^(\d+)', pa['resultado'] or '')
            enc['partidos'].append({
                'orden': pa['orden'],
                'tipo': 'fourball' if (pa['modalidad'] or '').lower().startswith('four') else 'individual',
                'lados': lados,
                'ganador': ganador,
                'margen': pa['resultado'],
                'ups': int(m.group(1)) if m else (1 if (pa['resultado'] or '').endswith('UP') else 0),
                'incomparecencia': None,
            })
        if nuestro:
            v = next((x for x in vj['partidos'] if x['fecha'] == e['fecha']), None)
            if v:
                enc['insId'] = v['id']
                # Las incomparecencias no estan en el acta: el 6 del reglamento
                # las salda con un 5&4, igual que una derrota jugada. Vienen de
                # csc.json, donde se anotaron a mano.
                for nom in v.get('incomparecencias', []):
                    for pa in enc['partidos']:
                        for lado in pa['lados']:
                            if nom in lado['jugadores']:
                                pa['incomparecencia'] = lado['equipo']
        encs.append(enc)

    # Los encuentros aun sin jugar no tienen acta, asi que vienen de csc.json.
    # Se guardan sin `partidos` y con el formato previsto, que es lo que el
    # microsite necesita para saber cuantos convocar.
    for p in vj['partidos']:
        if p['resultado'] is not None:
            continue
        fb = ind = 0
        for seg in p['formato'].split('+'):
            m = re.search(r'\d+', seg)
            n = int(m.group()) if m else 0
            if 'fourball' in seg: fb += n
            else: ind += n
        encs.append({
            'id': f"{lid}-{'cuartos' if p['id'].endswith('QF') else 'liga'}-{p['fecha']}",
            'fase': 'cuartos' if p['id'].endswith('QF') else 'liga',
            'grupo': None, 'jornada': None, 'vuelta': None,
            'fecha': p['fecha'], 'campo': p['campo'],
            'equipos': [{'nombre': 'Cuartillos', 'puntos': None, 'ups': None},
                        {'nombre': p['rival'], 'puntos': None, 'ups': None}],
            'formatoPrevisto': {'fourball': fb, 'individual': ind},
            'insId': p['id'],
            'partidos': [],
        })
    encs.sort(key=lambda e: e['fecha'] or '9999')

    ligas.append({
        'id': lid, 'nombre': vj['nombre'],
        'escenario': 16 if lid == 'ES' else 20,
        'nuestroGrupo': vj['grupo'],
        'grupos': grupos,
        'clasificatorio': {'fecha': vj['fechaClasificatorio'], 'campo': vj['campoClasificatorio'],
                           'posicion': vj['posClasificatorio'], 'puntos': vj['ptosClasificatorio'],
                           'jugadores': vj['jugadoresClasificatorio']},
        # altaRFGM: la fecha en que el jugador consta en la lista de la RFGM.
        # Los de la lista original van con el plazo del 11 del reglamento (10:00
        # del 16 de febrero); los anadidos despues, a null hasta que se confirme.
        # Medido contra el primer commit de csc.json: los unicos posteriores son
        # Jaime Villanueva, Marcos Ruiz y Nicolas Sequera, de alta el 2026-10-22.
        'elegibles': [{**x, 'altaRFGM': None if x['nombre'] in POSTERIORES else '2026-02-16'}
                      for x in vj['elegibles']],
        'encuentros': encs,
    })

out = {'temporada': 2026,
       'fuente': 'actas de nextcaddy, agrupaciones 13-26, bajadas el 2026-10-26',
       'ligas': ligas}
with open(SALIDA, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
    f.write('\n')

for l in ligas:
    nos = [e for e in l['encuentros'] if any(q['nombre'] == 'Cuartillos' for q in e['equipos'])]
    print(f"{l['id']}: {len(l['encuentros'])} encuentros ({len(nos)} nuestros), "
          f"{sum(len(e['partidos']) for e in l['encuentros'])} partidos, "
          f"{len(l['elegibles'])} elegibles")
