from time import sleep
galera = list()
dado = list()
while True:
    dado.append(str(input('nome:')))
    dado.append(float(input('peso:')))
    galera.append(dado[:])
    dado.clear()
    reposta = str(input('quer continuar? [S/N]')).upper().strip()[0]
    if reposta in 'N':
        print('programa encerrando!')
        print('aguarde para ver o resultado ')
        sleep(1)
        break
print(f'ao todo vc cadastrou  pessoas {len(galera)}')
idx, max_value = max(galera, key=lambda item: item[1])
print('o peso maximo foi de', max_value, "e foi de ", idx)
idx, min_value = min(galera, key=lambda item: item[1])
print('o peso minimo foi de', min_value, "e foi de ", idx)
