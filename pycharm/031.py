km = float(input('qual a distancia em (km) voce deseja percorrer?'))
if km <= 200:
    print(f'sua passagem vai custar R${km * 0.5} reais')
else:
    print(f'a sua passagem vai custar R${km * 0.45} reais')
