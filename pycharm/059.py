from time import sleep

primeiro_valor = int(input('primeiro valor:'))
segundo_valor = int(input('segundo valor:'))
pergunta = 0
while pergunta != 5:
    print('[1] para somar\n[2] para multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa')
    pergunta = int(input('>>>>qual a sua opcao?'))
    if pergunta == 1:
        print(f'a soma entre {primeiro_valor} + {segundo_valor} fica {primeiro_valor + segundo_valor}')
        print('--------------------------------------------------------')
    elif pergunta == 2:
        print(f'a multipliacao entre {primeiro_valor} * {segundo_valor} fica {primeiro_valor * segundo_valor}')
        print('--------------------------------------------------------')
    elif pergunta == 3:
        print(f'o maior entre {primeiro_valor} e {segundo_valor} e {max(primeiro_valor, segundo_valor)}')
        print('--------------------------------------------------------')
    elif pergunta == 4:
        print('informe os numeros novamente.')
        input('primeiro valor:')
        input('segundo valor:')
        print('--------------------------------------------------------')
    elif pergunta == 5:
        print('finalizando...')
    else:
        print('opcao invalida, tente um numero valido')
print('fechando o programa')
sleep(1)
