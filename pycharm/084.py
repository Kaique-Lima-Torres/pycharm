from time import sleep
pessoas = list()
dados = list()
pessoas_pesso = list()
while True:
    pessoas.append(str(input('nome: ')))
    peso = (float(input('peso: ')))
    continuacao = str(input('deseja continuar? [S/N]')).strip().upper()
    pessoas.append(peso)
    pessoas_pesso.append(peso)
    dados.append(pessoas[:])
    pessoas.clear()
    while continuacao not in 'SsNn':
        continuacao = str(input('Digite uma opcao valida [S/N]')).strip().upper()
    if continuacao == 'N':
        print('programa encerrando!')
        print('aguarde para ver o resultado ')
        sleep(1)
        break
print(f'ao todo vc cadastrou {len(dados)} pessoas')
maior_peso = list()
menor_peso = list()
for p in dados:
    if p[1] >= max(pessoas_pesso):
        maior_peso.append(p[0])
    elif p[1] <= min(pessoas_pesso):
        menor_peso.append(p[0])
print(f'o maior peso foi de {max(pessoas_pesso)}, e as pessaos foram {maior_peso}')
print(f'o menor peso foi de {min(pessoas_pesso)}, e as pessoas {menor_peso}')
