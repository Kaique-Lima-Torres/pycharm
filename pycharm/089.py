from time import sleep

alunos = list()
while True:
    nome = str(input('nome:'))
    nota1 = float(input('nota1:'))
    nota2 = float(input('nota2:'))
    media = (nota1 + nota2) / 2
    alunos.append(([nome, [nota1],]))
    continuacao = str(input('quer continuar [S/N]')).upper().strip()
    while continuacao not in 'SsNn':
        continuacao = str(input('digite uma resposta valida [S/N]')).upper().strip()
    if continuacao == 'N':
        print('encerrando o programa')
        print('espere para o seu resultado')
        sleep(1)
        break

print('*-*' * 15)
print(f'{"no.":<4}{"nome":<10}{"media":>8}')
print('-'* 20)
for p, v in enumerate(alunos):
    print(f"{p:<4}{v[0]:<10}{v[1][0]:>8.1f}")
while True:
    print('-' * 20)
    opcao = int(input('deseja ver a nota de qual aluno? [digite 999 para parar o programa]'))
    if opcao == 999:
        print('finalizando o programa...')
        sleep(1)
        break
    if opcao <= len(alunos)-1:
        print(f'notas de {alunos[opcao][0]} sao {alunos[opcao][1]}')
print('<<<<<BOA SORTE>>>>>')
