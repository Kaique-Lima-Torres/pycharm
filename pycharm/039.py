from datetime import date

atual = date.today().year
nasc = int(input('Qual seu ano de nascimento: '))
idade = atual - nasc

if idade < 18:
    dif = 18 - idade
    ano = atual + dif
    if dif > 1:
        print(f'Ainda faltam {dif} anos para o seu alistamento')
        print(f'Seu alistamento será em {ano}')
    else:
        print(f'Ainda falta {dif} ano para o seu alistamento')
elif idade > 18:
    dif = idade - 18
    ano = atual - dif
    if dif > 1:
        print(f'voce ja deveria ter se alistado há {dif} anos')
        print(f'o seu alistamento foi em {ano}')
    else:
        print('Voce deveria ter se alistado ano passado')
else:
    print('Voce deve se alistar esse ano')
