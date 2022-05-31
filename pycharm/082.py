from time import sleep
lista = []
par = []
impar = []
while True:
    lista.append(int(input('digite um numero:')))
    continuacao = str(input('vc deseja continuar? [S/N]')).upper().strip()
    while continuacao not in 'SsNn':
        continuacao = str(input('digite uma resposta valida [S/N]')).upper().strip()
    if continuacao == 'N':
        print('encerrando o programa')
        print('espere para o seu resultado')
        sleep(1)
        break
for v in lista:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('<--------------------------->')
print(f'a lista completa e {sorted(lista)}')
print(f'foi digitado par {par}')
print(f'digitado impar {impar}')
