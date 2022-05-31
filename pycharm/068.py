from random import randint
from time import sleep

voce_venceu = 0
computador_venceu = 0
jogada = 0
computador = randint(0, 10)

while True:
    jogador = int(input('digite um valor:'))
    opcao = str(input('par ou impar[P/I]')).upper()
    soma = jogador + computador
    print(f'vc jogou {jogador} e o computador jogou {computador} a soma deu {soma}')
    if opcao == 'P' and (soma % 2 == 0):
        sleep(1)
        print('vc venceu deu par')
        voce_venceu += 1
    else:
        sleep(1)
        print('vc perdeu')
        computador_venceu += 1
        print(f'o total de pontos que vc fez foi de {voce_venceu}')
        break
    if opcao == 'I' and (soma % 2 == 1):
        sleep(1)
        print('vc venceu deu impar')
        voce_venceu += 1
    else:
        sleep(1)
        print('vc perdeu')
        computador_venceu += 1
        print(f'o total de pontos que vc fez foi de {voce_venceu}')
        break
    print(f'vc ganhou {voce_venceu} vezes, e perdeu {computador_venceu} vezes')
