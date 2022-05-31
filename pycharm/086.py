matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for p in range(0, 3):
    for c in range(0, 3):
        matriz[p][c] = int(input(f'digite um valor para [{p},{c}]: '))
print('*-*' * 30)
for p in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[p][c]:^5}]', end='')
    print()
