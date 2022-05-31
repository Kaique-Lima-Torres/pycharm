from random import randint
from time import sleep

tentavivas = 0

computador = randint(0, 10)
palpite = ''
sleep(1 / 3)
while palpite != computador:
    palpite = int(input('qual e o seu palpite?'))
    tentavivas += 1
    if palpite == computador:
        print(f'vc acertou em {tentavivas} vezes')
        quit()
    if palpite <= computador:
        print('mais...')
    if palpite >= computador:
        print('menos...')
