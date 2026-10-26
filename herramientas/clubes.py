"""Tabla de alias de clubes. Las actas escriben 22 clubes de 81 formas distintas."""
import re, unicodedata

def pelado(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
    s = s.replace('’', '').replace("'", '')
    s = re.sub(r'[^a-z0-9]', '', s)
    for a in ('clubdegolf', 'clubgolf', 'cde', 'club', 'cg', 'golf'):
        if s.startswith(a): s = s[len(a):]
    for z in ('demadrid', 'spain'):
        if s.endswith(z): s = s[:-len(z)]
    for z in ('golfclub', 'golf'):
        if s.endswith(z) and len(s) > len(z) + 2: s = s[:-len(z)]
    return s

CLUBES = {
    'Cuartillos':          ['Cuartillos', 'Cuartillos CG', 'Cuartillos C.G.', 'CUARTILLOS CLUB DE GOLF'],
    'Foro 2000':           ['Foro 2000', 'FORO2000'],
    'Grow Golf':           ['Grow Golf', 'GROW GOLF CLUB'],
    'Club El Estudiante':  ['Club El Estudiante', 'El Estudiante', 'golf el estudiante'],
    'Approach y Putt':     ['Approach y Putt'],
    'Putt & Drive':        ['PUTT & DRIVE'],
    'Goldfers':            ['GOLDfers'],
    'CG Caminos':          ['CG CAMINOS', 'CLUB DE GOLF CAMINOS'],
    'Tres Cantos':         ['Tres Cantos', 'Tres Cantos Golf'],
    'GLX Golf':            ['GLX Golf'],
    'AEPJG':               ['AEPJG', 'ASOCIACIÓN ESPAÑOLA PERIODISTAS JUGADORES DE GOLF'],
    'Golf de Golfos':      ['CDE GOLFDEGOLFOS', 'GOLFDEGOLFOS'],
    'CG Colmenar Viejo':   ['Club Golf Colmenar Viejo', 'Club Golf Colmenar', 'C.G. Colmenar Viejo'],
    'Golf Sierra Norte':   ['Golf Sierra Norte'],
    'Sultanes del Swing':  ['SULTANES DEL SWING'],
    'CG Arganda':          ['CG ARGANDA', 'Arganda'],
    'Octopus Golf':        ['Octopus Golf'],
    'CD Banco de España':  ['Banco de España'],
    'Golf Getafe':         ['CLUB GOLF GETAFE'],
    'Los Lunes al Golf':   ['Los Lunes al Golf'],
    'Team & Friends':      ['TEAM & FRIENDS', 'TEAM&FRIENDS'],
    'Reanimación GC':      ['Reanimación Golf Club', 'Reanimación golf'],
    'Ingenieros Industriales': ['Ingenieros Industriales', 'CLUB INGENIEROS INDUSTRIALES',
                                'C.G. Ingenieros Industriales', 'INGENIEROS INDUSTRIALES DE MADRID'],
    'Golf Gentlemen’s':    ['Golf Gentlemen’s', 'Gentlemen’s', 'Gentlemen’s Spain',
                                'Golf Gentlemens Spain'],
}
TABLA = {}
for canon, formas in CLUBES.items():
    TABLA[pelado(canon)] = canon
    for f in formas: TABLA[pelado(f)] = canon

def club(nombre):
    return TABLA.get(pelado(nombre))
