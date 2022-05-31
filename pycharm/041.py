from datetime import date

ano_atual = date.today().year
nascimento = float(input('que ano voce nasceu?'))
idade = ano_atual - nascimento
print(f'o atleta tem {idade:.1f}')
if 1 <= idade <= 9:
    print('voce e mirim')
elif 10 <= idade <= 14:
    print('vc e infantil')
elif 15 <= idade <= 19:
    print('voce e junior')
elif 20 <= idade <= 25:
    print('voce senior')
else:
    print('voce e master')
