n1 = int(input('digite o primeiro numero:'))
n2 = int(input('digite o segundo numero:'))
n3 = int(input('digite o terceiro numero:'))
lista = [n1, n2, n3]
lista_ordenada = sorted(lista)
print(f'o menor numero e {lista_ordenada[0]}')
print(f'o maior numero e {lista_ordenada[-1]}')
