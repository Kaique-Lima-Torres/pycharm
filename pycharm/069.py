total_idade = 0
homem_cadastro = 0
idade_mulher = 0

while True:
    print('----------------------------------------------')
    print('cadastre uma pessoa')
    print('----------------------------------------------')
    idade = int(input('idade:'))
    sexo  = str(input('sexo: [M/F]')).upper()
    continuar = str(input('quer continuar: [S/N]')).upper()
    
    if continuar == 'N':
        break
    if sexo == 'M':
        homem_cadastro += 1
    if sexo == 'F' and idade <20:
        idade_mulher += 1
    if sexo == 'M' or 'F' and idade >= 18:
        total_idade +=1

print(f'o total de homem cadastrado foi de {homem_cadastro}')
print(f'o total de pessoas maior que 18 anos foi de {total_idade}')
print(f'o total de mulheres com menos de 20 anos sao de {idade_mulher}')