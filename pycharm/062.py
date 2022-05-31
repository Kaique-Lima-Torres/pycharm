primeiro = int(input('primeiro termo:'))
razao = int(input('razao da PA:'))
termo = primeiro
contador = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} > ', end=' ')
        termo += razao
        contador += 1
    print(' PAUSA ')
    mais = int(input('quantos termos vc quer mostrar a mais? digite 0 para finalizar'))
print(f'progressao finalizada com {total} de termos mostrada')
