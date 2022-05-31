import time

numero = int(input('informe um numero:'))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
time.sleep(1)
print(f'analisando o numero {numero}')
print(f'a unidade e {unidade}\na dezena e {dezena}\na centena e {centena}\no milhar e {milhar}')
