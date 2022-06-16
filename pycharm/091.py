from random import randint
from operator import itemgetter
from time import sleep

jogadores = dict()
for c in range(1, 5):
    jogadores[f"jogador {c}"] = randint(1, 6)
raking = dict()
print('\033[1;32m==VALORES SORTEADOS==\033[m')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
raking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)  # muito importe
print('*-*' * 30)
print('\033[1;32m==RAKING DOS JOGADORES==\033[m')
for i, v in enumerate(raking):  # tratar como uma lista, para deixar tudo enfileirado
    print(f'{i + 1} lugar: {v[0]} com {v[1]}.')
    sleep(1)
