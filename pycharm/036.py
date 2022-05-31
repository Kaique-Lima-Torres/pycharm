casa = float(input('valor da casa(R$)?'))
salario = float(input('salario do comprador(R$):'))
anos = int(input('quantos anos de financiamento'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'para pagar uma casa de R${casa:.2f} em {anos:.2f} anos\na prestcao sera de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')
