total = 0
numero = int(input('digite um numero:'))
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mo numero {numero} foi divisivel {total} vezes')
if total == 2:
    print('e por isso que ele e PRIMO')
else:
    print('e por isso que ele nao e PRIMO')
