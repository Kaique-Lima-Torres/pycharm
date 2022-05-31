import random
from time import sleep
import emoji
import sys

lista = ['PEDRA', 'PAPEL', 'TESOURA']
aleatorio = lista.index(random.choice(lista))
print('''\033[1;35mJOKENPO
\033[1;32m[1] para jogar\033[m
\033[1;31m[2]\033[m\033[1;31m para nao jogar\033[m''')
opcao = float(input('vc deseja jogar?'))
if opcao == 1:
    print('\033[1;32mo jogo vai comecar! BOA SORTE\033[m')
    print("+---------------------+")
    sleep(1)
elif opcao == 2:
    print(emoji.emojize('\033[1;35mDesculpe! VOLTE SEMPRE \033[m:broken_heart:', variant='emoji_type'))
    sys.exit(0)
print('''\033[0;32mpara iniciar o jogo digite um dos numeros abaixo\033[m
\033[35m[0] PEDRA
[1]PAPEL
[2]TESOURA\033[m''')
jogador = int(input('digite seu numero:'))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Número inválido. Tente novamente.')
else:
    sleep(1 / 2)
    print('\033[1;35mJO')
    sleep(1 / 2)
    print('KEN')
    sleep(1 / 2)
    print('PO\033[m')
print(f'\033[1;32mo computador escolheu {lista[aleatorio]}\033[m')
print(f'\033[1;32mvoce escolheu {lista[jogador]}\033[m')
if aleatorio == 0:
    if jogador == 0:
        print(emoji.emojize(' DEU EMPATE \033[1;34mJOKENPO\033[m :handshake_light_skin_tone:', variant='emoji_type'))
    elif jogador == 1:
        print(emoji.emojize('VC GANHOU \033[1;34mJOKENPO\033[m :1st_place_medal:', variant='emoji_type'))
    elif jogador == 2:
        print(emoji.emojize(' O COMPUTADOR VENCEU \033[1;34mJOKENPO\033[m :desktop_computer:', variant='emoji_type'))
if aleatorio == 1:
    if jogador == 1:
        print(emoji.emojize(' DEU EMPATE \033[1;34mJOKENPO\033[m :handshake_light_skin_tone:', variant='emoji_type'))
    elif jogador == 0:
        print(emoji.emojize(' O COMPUTADOR VENCEU \033[1;34mJOKENPO\033[m :desktop_computer:', variant='emoji_type'))
    elif jogador == 2:
        print(emoji.emojize('VC GANHOU \033[1;34mJOKENPO\033[m :1st_place_medal:', variant='emoji_type'))
if aleatorio == 2:
    if jogador == 2:
        print(emoji.emojize(' DEU EMPATE \033[1;34mJOKENPO\033[m :handshake_light_skin_tone:', variant='emoji_type'))
    elif jogador == 0:
        print(emoji.emojize('VOCE GANHOU \033[1;34mJOKENPO\033[m :1st_place_medal:', variant='emoji_type'))
    elif jogador == 1:
        print(emoji.emojize(' O COMPUTADOR VENCEU \033[1;34mJOKENPO\033[m :desktop_computer:', variant='emoji_type'))
        sys.exit()
print("+---------------------+")
print(emoji.emojize('OBRIGADO POR JOGAR \033[1;35mJOKENPO\033[m :red_heart:', variant='emoji_type'))
