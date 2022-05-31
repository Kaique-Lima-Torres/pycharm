dias = int(input('quantos dias o carro foi alugado?'))
km = float(input('quantos km foi rodado?'))
pagamento = (dias * 60) + (km * 0.15)
print(f'o total a se pagar vai ser de {pagamento:.2f}')
