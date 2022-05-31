valores = []
for p in range(0, 5):
    valores.append(int(input(f'Digite um valor na posicao {p + 1}:')))
maximo = valores.index(max(valores))
minimo = valores.index((min(valores)))
print(f'vc digitou os valores {valores}')
print(f'o maior valor digitado foi {max(valores)} na posicao {maximo + 1}')
print(f'o menor valor digitado foi {min(valores)} na posicao {minimo + 1}')
