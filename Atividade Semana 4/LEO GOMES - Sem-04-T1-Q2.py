def e_impar(n):
    return n%2 == 0

n = int(input('digite um número:'))
print(f'o número {n} é ímpar?', not e_impar(n))
