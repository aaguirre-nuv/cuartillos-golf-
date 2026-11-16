"""Lee de golfdirecto la informacion de los torneos pendientes: salidas, hora, precios.

Uso:  python herramientas/info_golfdirecto.py

Recorre datos/calendario.json y, para cada torneo sin jugar con urlGolfDirecto,
lee la API publica que usa el propio micrositio:
    https://www.golfdirecto.com/api/v2/public/game/<id>/active
El texto esta en data.microsite.information (HTML que escribe el organizador).
Solo imprime: los valores se pasan a mano a calendario.json (precio, hora,
observaciones). Medido el 2026-11-16 con el T9 y el T10: la API no publica
fecha de cierre de la inscripcion, y los campos de precio estructurados
(price, priceForGeneral) vienen vacios; el precio solo esta en ese texto.
"""
import html
import json
import re
import urllib.request

cal = json.load(open('datos/calendario.json', encoding='utf-8'))
for t in cal:
    url = t.get('urlGolfDirecto')
    if t.get('jugado') or not url:
        continue
    gid = re.search(r'/game/([0-9a-f]{24})', url).group(1)
    req = urllib.request.Request(f'https://www.golfdirecto.com/api/v2/public/game/{gid}/active',
                                 headers={'User-Agent': 'Mozilla/5.0'})
    d = json.load(urllib.request.urlopen(req, timeout=30))['data']
    info = (d.get('microsite') or {}).get('information') or ''
    texto = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', info))).strip()
    print(f"{t['id']} {t['fecha']} {t['campo']} | {d['name']} | {d['scheduleStartDate']} | {d['status']}")
    print(f"   {texto}")
