from datetime import date

menor = 0
for c in range(1, 8):
    nome = int(input('Digite o ano do seu nascimento:'))
    if date.today().year - nome > 18:
        menor += 1
        print(f'{menor} pessoas sao de maior')
    else:
        print(f'{menor} sao de menor')
