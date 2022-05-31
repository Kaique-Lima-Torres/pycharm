import calendar
from datetime import date
ano = int(input('digite o ano que vc quer analisar: coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
anobix = calendar.isleap(ano)
if anobix is True:
    print(f'o ano de {ano} e bissexto')
else:
    print(f'o ano de {ano} nao e bissexto')
