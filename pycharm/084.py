from time import sleep
galera = list()
dado = list()
while True:
    dado.append(str(input('nome:')))
    dado.append(float(input('peso:')))
    galera.append(dado[:])
    dado.clear()
    continuacao = str(input('vc deseja continuar? [S/N]')).upper().strip()
    while continuacao not in 'SsNn':
        continuacao = str(input('digite uma resposta valida [S/N]')).upper().strip()
    if continuacao == 'N':
        print('encerrando o programa')
        print('espere para o seu resultado')
        sleep(1)
        break
print(f'ao todo vc cadastrou  pessoas {len(galera)}')
idx, max_value = max(galera, key=lambda item: item[1])
print('o peso maximo foi de', max_value, "e foi de ", idx)
idx, min_value = min(galera, key=lambda item: item[1])
print('o peso minimo foi de', min_value, "e foi de ", idx)
