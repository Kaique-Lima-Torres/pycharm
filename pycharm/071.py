print(f'bem vindo ao banco digital')
while True:
    valor = int(input('digite um valor inteiro para ser sacado. R$'))
    continuacao = str(input('voce deseja continuar? [S/N]')).upper().strip()
    if continuacao == 'N':
        break
    nota50 = valor // 50
    valor %= 50
    nota20 = valor // 20
    valor %= 20
    nota10 = valor // 10
    valor %= 10
    nota5 = valor // 5
    valor %= 5
    nota1 = valor // 1
    valor %= 1
    print(f'voce sacou\n{nota50} notas de 50\n{nota20} notas de 20\n{nota10} notas de 10\n{nota5} notas de 5\n{nota1} notas de 1')
