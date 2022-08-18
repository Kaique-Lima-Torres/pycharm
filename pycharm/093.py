dados = dict()

dados['nome'] = str(input('Nome do Jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
dados['gols'] = list()
for c in range(0, dados['partidas']):
    dados['gols'].append(int(input(f'Quantos gols na partida {c + 1}? ')))
dados['total'] = sum(dados['gols'])
print('*-*' * 30)
print(dados)
print('*-*' * 30)
for i, v in dados.items():
    print(f'o campo {i} tem o valor de {v}')
print('*-*' * 30)
print(f'o jogador {dados["nome"]} jogou {dados["partidas"]} partidas')
for c in range(0, dados['partidas']):
    print(f' =>> na partida {c + 1} ele marcou {dados["gols"][c]} gols')
print(f'o {dados["nome"]} fez um total de {dados["total"]} gols')
