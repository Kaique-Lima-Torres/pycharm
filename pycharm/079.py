from time import sleep
from collections import OrderedDict

numero = []
while True:
    numero.append(int(input('Digite um Valor:')))
    print('Valor adicionado com sucesso')
    continuacao = str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuacao == 'N':
        print('programa encerrando,obrigado')
        sleep(1)
        break
final_list = list(OrderedDict.fromkeys(numero))
print(f'os valores digitados foram{sorted(final_list)}')
