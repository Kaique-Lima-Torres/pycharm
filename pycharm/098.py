def contador(incio, fim, passo):
    print(f'contagem de {incio} ate {fim} de {passo} em {passo}')

    if incio < fim:
        cont = incio
        while cont <= fim:
            print(f'{cont}',end=' ')
            cont += passo
        print('fim')

    else:
        cont = incio
        while cont >= fim:
            print(f'{cont}',end=' ')
            cont -= passo
        print('fim')


# programa principal
contador(1, 10, 1)
contador(10, 1, 2)
inicio = int(input('inicio:'))
fim = int(input('fim:'))
passo = int(input('passo:'))
contador(inicio,fim,passo)