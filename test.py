import random

def generate_feistel_key(text: str) -> tuple:
    # Diviser le texte brut binaire en deux moitiés
    left_half = text[:len(text)//2]
    right_half = text[len(text)//2:]

    # Générer des clés binaires aléatoires pour les deux tours
    k1 = ''.join(random.choice(['0', '1']) for _ in range(len(text)//2))
    k2 = ''.join(random.choice(['0', '1']) for _ in range(len(text)//2))

    return (left_half, right_half, k1, k2)

def feistel_cipher_encrypt_decrypt(text: str, key: str, rounds: int) -> str:
    # Diviser le texte brut binaire en deux moitiés
    left_half = text[:len(text)//2]
    right_half = text[len(text)//2:]

    # Générer des clés binaires aléatoires pour les deux tours
    keys = [key[i:i+len(text)//2] for i in range(0, len(key), len(text)//2)]

    # Effectuer les tours de chiffrement
    for i in range(rounds):
        # Calculer la fonction F
        f = int(right_half, 2) ^ int(keys[i], 2)
        f = bin(f)[2:].zfill(len(right_half))

        # Échanger les moitiés
        left_half, right_half = right_half, bin(int(left_half, 2) ^ int(f, 2))[2:].zfill(len(right_half))

    # Inverser les moitiés
    encrypted_text = right_half + left_half

    return encrypted_text

def text_to_binary(text: str) -> str:
    binary = ''
    for char in text:
        binary += bin(ord(char))[2:].zfill(8)
    return binary

text = text_to_binary('Bonjour, comment ça va ?')
key = generate_feistel_key('11010011')
rounds = 16

print (key)
# Chiffrement
# encrypted_text = feistel_cipher_encrypt_decrypt(text, key, rounds)
# print(f'Chiffré: {encrypted_text}')

# Déchiffrement
# decrypted_text = feistel_cipher_encrypt_decrypt(encrypted_text, key, rounds)
# print(f'Déchiffré: {decrypted_text}')

################################################################

def feistel_algorithm(K):
    # Appliquer la fonction de permutation H = 65274130
    H = [6, 5, 2, 7, 4, 1, 3, 0]
    K = [K[i] for i in H]

    # Diviser K en deux blocs de 4 bits : K = k′1||k′2
    k1 = K[:4]
    k2 = K[4:]

    # k1 = k′1 ⊕k′2 et k2 = k′2 ∧ k′1
    k1 = [k1[i] ^ k2[i] for i in range(4)]
    k2 = [k2[i] & k1[i] for i in range(4)]

    # Appliquer le décalage à gauche d’ordre 2 pour k1 et le décalage à droite d’ordre 1 pour k2
    k1 = k1[2:] + k1[:2]
    k2 = k2[-1:] + k2[:-1]

    # Sortie : Deux sous-clés (k1 , k2) de longueur 4.
    return k1, k2

# Exemple d'utilisation
K = [1, 2, 3, 4, 5, 6, 7, 8]
k1, k2 = feistel_algorithm(K)
print(f"Sous-clé 1 : {k1}")
print(f"Sous-clé 2 : {k2}")
