from time import sleep

numero = []
while True:
    numero.append(int(input('Digite um Valor:')))
    print('Valor adicionado com sucesso')
    continuacao = str(input('Deseja continuar? [S/N]')).strip().upper()
    while continuacao not in 'SsNn':
        continuacao = str(input('digite uma resposta valida [S/N]')).strip().upper()
    if continuacao == 'N':
        print('programa encerrando,obrigado')
        print('espere para o seu resultado')
        sleep(1)
        break
print(f'voce digitou {len(numero)} elementos')
print(f'os valores em ordem decrescente sao {sorted(numero, reverse=True)}')
if 5 not in numero:
    print('o valor 5 nao faz parte da lista')
else:
    print(f'o valor 5 faz parte da lista')
