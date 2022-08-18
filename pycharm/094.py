dados = dict()
galera = list()
media = soma = 0
while True:
    dados.clear()
    dados['nome'] = str(input('nome:'))
    while True:
        dados['sexo'] = str(input('sexo: [M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO!!, digite um sexo valido [M/F]')
    dados['idade'] = int(input('idade:'))
    soma += dados['idade']
    galera.append(dados.copy())
    while True:
        resposta = str(input('quer continuar? [S/N]')).upper()
        if resposta in 'SN':
            break
        print('ERRO!!, digite uma resposta valida [S/N]')
    if resposta == 'N':
        break
print('*-*'*30)
print(f'ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'a media de idade e de {media:5.2f}')
print('as mulheres cadastradas foram ',end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k,v in p.items():
            print(f'{k} = {v}: ',end='')