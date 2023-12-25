# 
# fait par MUSHAGALUSA MURHULA Ines
# 
# dirigé par l'assistant KANIGINI Junior
# dans le cadre du cours de cryptographie
# 

def square_and_multiply(x:int, b: int, n: int):
    b = bin(b).replace('0b', '')
    result = 0
    mod = 0

    for bit in b:
        if result < 2:
            result += 1
            mod = pow(x, result) % n
        else:
            result *= 2
            mod = pow(x, result) % n

        if bit == '1' and result > 2:
            result += 1
            mod = pow(x, result) % n

    return mod

print('Nous resolvont x^b (mod n) en utilisant l’algorithme des carrés et des multiplications\n')

x = int(input('Entrez la valeur de x: '))
b = int(input('Entrez la valeur de b: '))
n = int(input('Entrez la valeur de n: '))

r = square_and_multiply(x, b, n)

print(f'{x}^{b} (mod {n}) = {r}')