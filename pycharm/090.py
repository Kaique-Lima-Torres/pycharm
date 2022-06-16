from time import sleep

aluno = dict()
escola = list()
for c in range(0,1):
    aluno['nome'] = str(input('nome:'))
    aluno['media'] = float(input(f'media de {aluno["nome"]}:'))
    if aluno['media'] >= 7:
        sleep(1)
        print('\033[1;32maprovado\033[m')
    else:
        sleep(1)
        print('\033[1;31mreprovado\033[m')
        print('a media da escola e de [7.0]')
print(f'o aluno {aluno["nome"]} tem a media de {aluno["media"]}')
