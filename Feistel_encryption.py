# 
# fait par MUSHAGALUSA MURHULA Ines
# 
# dirigé par l'assistant KANIGINI Junior
# dans le cadre du cours de cryptographie
# 

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
    n1 = n[:4]
    n2 = n[4:]

    return n1, n2

def inverse (key: str) -> str:
    tab = []

    for k in key:
        tab.append(k)

    tab.reverse()
    key = ''

    for k in tab:
        key += k

    return key

def generate_key(key: str, h: str = '65274130'):
    """genere une clé pour le chiffrement de Feistel"""

    key = permute(key, h) # application de la fonction de permutation 
    k1, k2 = splitor(key) # division en deux bloc
    k1, k2 = int(k1, 2), int(k2, 2)
    k = k1 ^ k2 # k1′ ⊕ k2′
    k2 = bin(k1 & k2).replace('0b', '').zfill(4) # k2′ ∧ k1′
    k1 = bin(k).replace('0b', '').zfill(4)
    k1 = k1[2:] + k1[:2] # décalage à gauche d’ordre 2
    k2 = k2[-1:] + k2[:-1] # décalage à droite d’ordre 1
    return k1, k2

def encryption (bloc: str, key:str, h = '46027315'):
    """Chiffre le bloc avec le chiffrement de Feistel"""

    p = '2013'
    bloc = permute(bloc, h) # application de la fonction de permutation 
    k1, k2 = generate_key(key) # generation de clé
    k1, k2 = int(k1, 2), int(k2, 2)
    g0, d0 = splitor(bloc) # division en deux bloc
    g0, d0 = int(g0, 2), int(d0, 2)
    g0 = bin(g0).replace('0b', '').zfill(4)

    # round 1
    g0 = int(permute(g0, p), 2)
    d1 = g0 ^ k1
    g1 = bin(d0 ^ (g0 | k1)).replace('0b', '').zfill(4)

    # round 2
    g1 = int(permute(g1, p), 2)
    d2 = bin(g1 ^ k2).replace('0b', '').zfill(4)
    g2 = bin(d1 ^ (g1 | k2)).replace('0b', '').zfill(4)

    c = g2 + d2
    c = permute(c, inverse(h)) # application de la fonction inverse de la permutation
    return c

def decryption (bloc: str, key: str, h = '46027315'):
    p = inverse('2013')
    g2, d2 = splitor(bloc)
    g2, d2 = int(g2, 2), int(d2, 2)
    k1, k2 = generate_key(key)
    k1, k2 = int(k1, 2), int(k2, 2)

    # round 1
    g1 = bin(d2 ^ k2).replace('0b', '').zfill(4)
    g1 = int(permute(g1, p), 2)
    d1 = g2 ^ (g1 | k2)

    # round 2
    g0 = bin(d1 ^ k1).replace('0b', '').zfill(4)
    g0 = int(permute(g0, p), 2)
    d0 = bin(g1 ^ (g0 | k1)).replace('0b', '').zfill(4)
    g0 = bin(g0).replace('0b', '').zfill(4)
    
    n = g0 + d0
    n = permute(n, inverse(h))
    return n

while True:
    k = input('Entez la clé à partir du quel nous genererons la clé de feistel (un mot de 8 bits svp): ')
    n = input('Entrez le mot de 8 bits à chiffré :')

    if len(k) != 8 and len(n) != 8:
        print('Vous devez respecter la longueur 8 par exemple 10011011\n')
    else : break

subkeys = generate_key(k)
encript = encryption(n, k)
decript = decryption(encript, k)

print(f'les deux sous-clés generer sont {subkeys}')
print(f'le version chiffré de {n} est {encript}')
print(f'le dechiffage est {decript}\n')

print('Merci d\'avoir utiliser notre programme')

"""
il est à remqarqué qu'en dichiffrant nous ne retrouvons pas le mot entrer en claire malgrés
le suivi stricte de l'algorithme donnée.

veulliez me donnée la correction svp
"""