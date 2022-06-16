matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = colun3 = 0
for p in range(0, 3):
    for c in range(0, 3):
        matriz[p][c] = int(input(f'digite um valor para [{p},{c}]: '))
        par += matriz[p][c] if matriz[p][c] % 2 == 0 else 0
        colun3 += matriz[p][c] if c == 2 else 0
print('*-*' * 30)
for p in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[p][c]:^5}]', end='')
    print()
print(f'os numeros pares sao {par}')
print(f'a soma do valor da 3 coluna e {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'o maior valor da 2 linha e {max(matriz[1])}')
