lista = []
media = cont = soma = 0
r = 'S'
while r == 'S':
    n = int(input('digite um valor:'))
    r = str(input('quer continuar? [S/N]')).upper()
    cont += 1
    soma += n
    lista += [n]
print(f'o total de numeros que vc digitou foi de {cont} a media foi de {soma/cont}')
print(f'o valor maximo foi {max(lista)} e o minimo de {min(lista)}')
