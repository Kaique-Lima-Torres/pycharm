from ex100 import moeda

num = int(input('digite um valor:'))
print(f'o numero que foi digitado foi R${num} ')
print(f'o dobro de R${num} e R${moeda.dobro(num)}')
print(f'a metade de R${num} e de R${moeda.metade(num)}')
print(f'aumentando 10%, temos R${moeda.aumentar(num)}')
print(f'reduzindo 13%, temos R${moeda.diminuir(num)}')