lista_preco = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
print('-'*40)
print(f'\033[1;32mBEM VINDO A LISTA DE PRECO\033[m')
print('-'*40)
for pos in range(0, len(lista_preco)):
    if pos % 2 == 0:
        print(f'{lista_preco[pos]:.<30}', end='')
    else:
        print(f'R${lista_preco[pos]:.>7.2f}')
print('-'*40)
