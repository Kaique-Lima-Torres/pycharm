from random import randint
lista = []
print('*-*' * 15)
print('    BEM VINDO A MEGA SENA     ')
print('*-*' * 15)
jogos = int(input('quantos jogos vc quer?'))
for c in range(1,jogos + 1):
    n1 = randint(1, 60)
    n2 = randint(1, 60)
    n3 = randint(1, 60)
    n4 = randint(1, 60)
    n5 = randint(1, 60)
    n6 = randint(1, 60)
    lista = [n1, n2, n3, n4, n5, n6]
    print(f'Jogo {c}: {sorted(lista)}')


