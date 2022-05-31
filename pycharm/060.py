# 1 metodo usando funcao
# from math import factorial
numero = int(input('digite um numero para encontrar seu fatorial:'))
# print(factorial(numero))

# 2 metodo
c = numero
f = 1
while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
