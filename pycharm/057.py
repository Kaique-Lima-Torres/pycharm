sexo = str(input('informe seu sexo: [M/F]')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados invalidos. por favor, informe seu sexo:')).upper().strip()[0]
print(f'sexo {sexo} registrado com sucesso')
