from random import randint

def sorteio(lista):
    print('analisando os numeros passando...')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}',end=' ')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma+=valor
    print(f'somando os valores de pares temos {lista}, temos {soma}')
numero = list()
sorteio(numero)
somapar(numero)


