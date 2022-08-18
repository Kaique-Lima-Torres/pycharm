from time import sleep
from datetime import datetime

print('-=-' * 20)
todos = list()
nome_usuario = str(input('qual o nome do usuario?')).lower()
print(f'Bem vindo ao programa {nome_usuario}, obrigado por usar meu programa')
print(f'a data de hoje é {datetime.today()}')
sleep(2)
while True:
    jogador = dict()
    nome = input('Nome do jogador: ').strip()
    npart = int(input(f'Quantas partidas {nome} jogou? '))
    gols = list()
    tot = 0
    for c in range(1, npart + 1):
        p = int(input(f'   -Gols na {c}ª partida: '))
        gols.append(p)
        tot += p
    jogador = {
        'nome': nome,
        'gols': gols,
        'total': tot
    }
    todos.append(jogador.copy())
    opc = input('Quer continuar? [S/N] ').strip().lower()
    if opc != 's' and opc != 'n':
        print('\033[31mERRO: Digite apenas S ou N (SIM ou NÃO)\033[m')
        while opc != 's' and opc != 'n':
            opc = input('Quer continuar? [S/N] ').strip().lower()
    if opc == 'n':
        break
print(f'aguarde o programa para monstrar a lista dos jogadores')
sleep(2)
print(f'{"-=-" * 20}\ncod nome{" " * 11}gols{" " * 11}total\n{"-" * 40}')
for j in todos:
    sla = f'{todos.index(j):>3} {j["nome"]}{" " * (20 - len(j["nome"]) - 5)}{j["gols"]}'
    print(f'{sla}{" " * (34 - len(sla))}{j["total"]}')
while True:
    print('-' * 40)
    opt = int(input('Mostrar dados de qual jogador? [Digite 999 para sair] '))
    if opt < 0 or opt > len(todos) - 1:
        while opt < 0 or opt > len(todos) - 1:
            if opt == 999:
                break
            print(f'\033[31mERRO: Não existe jogador com o código {opt}.\033[m')
            opt = int(input('Mostrar dados de qual jogador? [Digite 999 para sair] '))
    if opt == 999:
        print('programa sendo finalizado!!')
        sleep(2)
        break
    for i in todos:
        if opt == todos.index(i):
            print(f'  -- Levantamento do Jogador {i["nome"]}')
            for jog in range(0, len(i['gols'])):
                print(f'    >> No jogo {jog + 1} fez {i["gols"][jog]} gols')
print(f'{"-" * 40}\n<<< VOLTE SEMPRE >>>')