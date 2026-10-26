"""Clasificacion de todos los grupos a partir de datos/csc2.json.

Sirve de verificacion del modelo nuevo: nuestras cifras tienen que salir
identicas a las de csc.json y a las que publico la RFGM.
"""
import json
import sys
from collections import defaultdict

N = json.load(open(sys.argv[1] if len(sys.argv) > 1 else 'datos/csc2.json', encoding='utf-8'))
REF = {'ES': (2.0, 15.0, (51, 35)), 'FS': (2.0, 13.5, (37, 25))}
fallos = []

for L in N['ligas']:
    print(f"\n########## {L['nombre']} · escenario de {L['escenario']} equipos")
    for g in L['grupos']:
        enc = [e for e in L['encuentros'] if e['grupo'] == g['id']]
        par = defaultdict(list)
        for e in enc:
            par[tuple(sorted(q['nombre'] for q in e['equipos']))].append(e)
        pts = {t: 0.0 for t in g['equipos']}
        gan = {t: 0.0 for t in g['equipos']}
        uf = {t: 0 for t in g['equipos']}
        uc = {t: 0 for t in g['equipos']}
        pend = []
        for (a, b), xs in par.items():
            s = {a: 0.0, b: 0.0}
            u = {a: 0, b: 0}
            for e in xs:
                d = {q['nombre']: q for q in e['equipos']}
                for t in (a, b):
                    s[t] += d[t]['puntos']
                    u[t] += d[t]['ups']
            for t, o in ((a, b), (b, a)):
                gan[t] += s[t]
                uf[t] += u[t]
                uc[t] += u[o]
            if len(xs) < 2:
                pend.append(f'{a}–{b}')
                continue
            if s[a] > s[b]: pts[a] += 1
            elif s[b] > s[a]: pts[b] += 1
            else: pts[a] += .5; pts[b] += .5
        etiq = g['nombre'] or f"({g['id']}, numero federativo desconocido)"
        print(f"  -- {etiq}" + (f"   SIN JUGAR: {', '.join(pend)}" if pend else ''))
        orden = sorted(g['equipos'], key=lambda t: (-pts[t], -gan[t], -(uf[t] - uc[t])))
        for i, t in enumerate(orden, 1):
            mio = '  <<<' if t == 'Cuartillos' else ''
            print(f"     {i}. {t:<22} {pts[t]:>4} pts | ganados {gan[t]:>5} | ups {uf[t]:>3}-{uc[t]:<3}{mio}")
        if g['nuestro']:
            p_, g_, u_ = REF[L['id']]
            for q, a, b in (('puntos', pts['Cuartillos'], p_),
                            ('partidos ganados', gan['Cuartillos'], g_),
                            ('ups', (uf['Cuartillos'], uc['Cuartillos']), u_)):
                if a != b: fallos.append(f"{L['id']} {q}: {a} != {b}")

print('\n' + ('VERIFICACION OK: las cifras de Cuartillos coinciden con csc.json y con la RFGM'
              if not fallos else 'FALLOS: ' + '; '.join(fallos)))
