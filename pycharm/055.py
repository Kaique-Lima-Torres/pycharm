acumulador = []
for c in range(1, 6):
    lista = float(input(f'o peso da {c} pessoa:'))
    acumulador += [lista]
print('o maior peso foi de:', max(acumulador))
print('o menor peso foi de:', min(acumulador))
