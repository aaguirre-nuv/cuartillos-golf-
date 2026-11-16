"""Baja actas de nextcaddy y las mete en docs/fuentes/nextcaddy-2026.json.

Uso:  python herramientas/bajar_actas.py <agrupacion> <liga> <fase> <id> [<id> ...]
Ej.:  python herramientas/bajar_actas.py 26 FS cuartos 74743 74746 74747 74748

Cada acta (https://www.nextcaddy.com/<id>/ryder-cup/livescoring) lleva el resultado
entero en un JSON embebido en el atributo data-symfony--ux-react--react-props-value.
Los ids de una jornada salen de https://www.nextcaddy.com/agrupacion/<n> (enlaces
/tour/<id>). Un acta ya presente con el mismo id se sustituye, no se duplica.
Escrito el 2026-11-16 para cargar los cuartos de fin de semana; las jornadas
anteriores se bajaron el 2026-10-26 con un guion que no quedo en el repo.
"""
import html
import json
import re
import sys
import urllib.request

FUENTE = 'docs/fuentes/nextcaddy-2026.json'
agrupacion, liga, fase, ids = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4:]


def acta(cid):
    req = urllib.request.Request(f'https://www.nextcaddy.com/{cid}/ryder-cup/livescoring',
                                 headers={'User-Agent': 'Mozilla/5.0'})
    page = urllib.request.urlopen(req, timeout=30).read().decode('utf-8')
    m = re.search(r'data-symfony--ux-react--react-props-value="([^"]+)"', page)
    if not m:
        raise SystemExit(f'{cid}: sin JSON embebido')
    d = json.loads(html.unescape(m.group(1)))['data']
    teams = d['teams']
    fecha, partidos = None, []
    for r in sorted(d['rounds'].values(), key=lambda r: r['order']):
        for mt in sorted(r['matches'].values(), key=lambda x: x['order']):
            fecha = fecha or mt['date']['date'][:10]
            if not mt.get('result'):
                continue
            partidos.append({
                'ronda': r['order'], 'modalidad': r['modality'], 'orden': mt['order'],
                'resultado': mt['result'],
                'finalizado': mt.get('finalized'),
                'lados': [{'equipo': teams[str(s['teamId'])]['name'],
                           'gana': bool(s['is_winner']),
                           'jugadores': [re.sub(r'\s+', ' ', f"{p['name']} {p['surname']}").strip()
                                         for p in s['players']]}
                          for s in mt['sides'].values()],
            })
    return {
        'agrupacion': agrupacion, 'liga': liga, 'fase': fase, 'id': int(cid),
        'nombre': d['competition']['name'], 'campo': d['competition'].get('hostName'),
        'fecha': fecha,
        'equipos': [{'id': tid, 'nombre': t['name'],
                     'puntos': t['score'].get('general'), 'ups': t['score'].get('ups')}
                    for tid, t in teams.items()],
        'partidos': partidos,
    }


E = json.load(open(FUENTE, encoding='utf-8'))
for cid in ids:
    a = acta(cid)
    E = [e for e in E if e['id'] != a['id']] + [a]
    eq = ' - '.join(f"{q['nombre']} {q['puntos']} ({q['ups']} ups)" for q in a['equipos'])
    print(f"{cid} {a['fecha']} {a['nombre']}: {eq}, {len(a['partidos'])} partidos")
with open(FUENTE, 'w', encoding='utf-8') as f:
    json.dump(E, f, ensure_ascii=False, indent=1)
    f.write('\n')
