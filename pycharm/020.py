import random
import time

n1 = str(input('primeiro aluno:'))
n2 = str(input('segundo aluno'))
n3 = str(input('terceiro aluno'))
n4 = str(input('quarto aluno'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
time.sleep(1)
print(f'a ordem de apresentacao sera de {lista}')