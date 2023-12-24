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
