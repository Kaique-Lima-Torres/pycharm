print('>>>>> GERADOR DE PA <<<<<')
primeiro = int(input('primeiro termo:'))
razao = int(input('razao da PA:'))
termo = primeiro
contador = 1
while contador <= 10:
    print(f'{termo} >', end=' ')
    termo += razao
    contador += 1
print('fim')
