numero = int(input('quantos termos vc quer mostrar:'))
primeiro_termo = 0
segundo_termo = 1
print(f'{primeiro_termo}, {segundo_termo},', end=' ' )
contador = 3
while contador <= numero:
    t3 = primeiro_termo + segundo_termo
    print(f'{t3},',end=' ')
    primeiro_termo = segundo_termo
    segundo_termo = t3
    contador +=1
print('fim')
