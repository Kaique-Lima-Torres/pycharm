aluno = dict()
for c in range(0, 1):
    aluno['nome'] = str(input('nome:'))
    aluno['media'] = float(input('media:'))
if aluno['media'] > 7:
    print(f'o aluno {aluno["nome"]} passou. o aluno esta com a media de {aluno["media"]}')
elif aluno['media'] == 7:
    print(f'o aluno {aluno["nome"]} precisa melhorar, o aluno esta com a media de {aluno["media"]}')
    print('a media da escola e de 7')
else:
    print(f'o aluno {aluno["nome"]} foi reprovado. o aluno esta com a media de {aluno["media"]}')
    print('a media da esocla e de 7')
