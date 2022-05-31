lista_nome = []
lista_nome_homem = []
lista_idade = []
lista_sexo = []
lista_idade_homem = []
lista_idade_mulher = []

for c in range(1, 5):
    print(f'>>> NOME DA {c} PESSOA <<<')
    nome = str(input('nome:')).strip().upper()
    lista_nome.append(nome)

    idade = int(input('idade:'))
    lista_idade.append(idade)

    sexo = str(input('sexo M/F:')).strip().upper()
    lista_sexo.append(sexo)

    if sexo == 'M':
        lista_nome_homem.append(nome)
        lista_idade_homem.append(idade)
    if sexo == 'F' and idade < 20:
        lista_idade_mulher.append(idade)

print(f'a media de idade do grupo e de {sum(lista_idade)/len(lista_idade)}')
print(f'o homem mais velho tem {max(lista_idade_homem)} anos e se chama {(lista_nome_homem[lista_idade_homem.index(max(lista_idade_homem))])}')
print(f'ao todo sao {len(lista_idade_mulher)} mulheres abaixo dos 20 anos')
