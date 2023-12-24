def permute (key: str, h: str) -> str:
    """Fait une permutation de la clé en fonction du pi (h)"""
    
    tab1 = []
    tab2 = []

    for k in key:
        tab1.append(k)

    for i in h:
        tab2.append(tab1[int(i)])

    key = ''

    for k in tab2:
        key += k

    return key

def splitor (n: str):
    """Divise l'arguments en 2 blocs de 4
    >>> splitor('10010110')
    ('1001', '0110')
    """
    n1 = int(n[:4], 2)
    n2 = int(n[4:], 2)

    return n1, n2

def generate_key(key: str, h: str = '65274130'):
    """genere une clé pour le chiffrement de Feistel"""

    key = permute(key, h)
    k1, k2 = splitor(key)
    k = k1 ^ k2
    k2 = bin(k1 & k2).replace('0b', '').zfill(4)
    k1 = bin(k).replace('0b', '').zfill(4)
    k1 = k1[2:] + k1[:2]
    k2 = k2[-1:] + k2[:-1]
    return k1, k2

def encryption (bloc: str, key:str, h = '46027315'):
    """Chiffre le bloc avec le chiffrement de Feistel"""

    p = '2013'
    bloc = permute(bloc, h)
    k1, k2 = generate_key(key)
    g0, d0 = splitor(bloc)
    g0 = bin(g0).zfill(4)
    d0 = bin(d0).zfill(4)
    g0 = int(permute(g0, p), 2)
    d1 = g0 ^ k1
    g1 = d0 ^ (g0 | k1)
    g1 = int(permute(g1, p), 2)
    d2 = bin(g1 ^ k2).zfill(4)
    g2 = bin(d1 ^ (g1 | k2)).zfill(4)
    c = g2 + d2
    # C'est ici où il manque la fonction d'inversion de la clé
    return c


