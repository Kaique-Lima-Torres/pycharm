from random import choice
import time

print('vou pensar em um numero entre 0 e 5. tente adivinhar!')
lista = [1, 2, 3, 4, 5]
escolha = choice(lista)
n1 = int(input('em que numero eu pensei?'))
print('processado...')
time.sleep(1)
if n1 == escolha:
    print('\033[1;32mPARABENS!\033[m VOCE VENCEU')
else:
    print('\033[1;31mVOCE PERDEU\033[m')
