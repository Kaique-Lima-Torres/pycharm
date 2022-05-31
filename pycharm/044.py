preco = float(input('qual o valor da sua compra? em R$'))
print('''FORMAS DE PAGAMENTO)
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('qual a sua opcao?'))
if opcao == 1:
    novo = preco - (preco * 10 / 100)
    print(f'o preco a vista no dinheiro/cheque, com 10% de desconto fica R${novo:.2f}')
elif opcao == 2:
    novo2 = preco - (preco * 5 / 100)
    print(f'o preco a vista com cartao, com 5% de desconto fica R${novo2:.2f}')
elif opcao == 3:
    print(f'o preco em ate 2x no cartao, fica em R${preco:.2f}')
elif opcao == 4:
    novo4 = preco + (preco * 20 / 100)
    total_pacerla = int(input('quantas parcelas?'))
    parcela = novo4 / total_pacerla
    print(f'sua compra sera parcelada em {total_pacerla}x, com 20% de juros fica {total_pacerla} parcelas de R${parcela:.2f}')
else:
    print('\033[1;31mopcao invalida, escolha uma das 4 opcoes\033[m')
