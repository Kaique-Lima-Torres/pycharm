print("+---------------------+")
print('10 TERMOS DE UMA PA')
print("+---------------------+")
primeiro = int(input('primeiro termo:'))
razao = int(input('razao:'))
for c in range(1, 11):
    n1 = primeiro + (c - 1) * razao
    print(n1)
