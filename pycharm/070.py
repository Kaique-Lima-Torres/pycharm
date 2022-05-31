produto_barato = []
total_compra = []
compra_acima = []
while True:
    nome = str(input('digite o nome do produto:'))
    preco = int(input('digite o preco do produto R$:'))
    total_compra.append(preco)
    produto_barato.append(nome)
    continuacao = str(input('deseja continuar [S/N]')).upper().strip()[0]
    if continuacao == 'N':
        break
    if preco >= 1000:
        compra_acima.append(preco)
print(f'o total da compra foi de R${sum(total_compra)}')
print(f'os produtos que custam mais de R$1.000 sao {len(compra_acima)}')
print(f'o produto mais barato se chama {produto_barato[total_compra.index(min(total_compra))]} e custa {min(total_compra) }')