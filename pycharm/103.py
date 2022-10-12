def lista(n='desconhecido', gol=0):
    print(f'o nome do jogador e {n} e o total de gols e {g}')


n = str(input('nome do jogador:'))
g = str(input('gols:'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    lista(gol=g)
else:
    lista(n, g)
