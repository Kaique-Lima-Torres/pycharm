valores = [[], []]
for v in range(0, 7):
    valor = int(input(f'digite o {v + 1} valor:'))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print(f'os valores pares digitados foram {sorted(valores[0])}')
print(f'os valores impares digitados foram {sorted(valores[1])}')
