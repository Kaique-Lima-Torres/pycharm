cont = 0
while True:
    n = int(input('digite um numero: digite [0] para sair do programa'))
    cont += 1
    if n <= -1:
        break
    elif n == 0:
        break
    for c in range(1, 11):
        print(f'{n}x{c}= {n * c}')
print('acabou')
