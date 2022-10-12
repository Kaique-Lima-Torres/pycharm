def voto(idade_atual):
    from datetime import date
    data_atual = date.today().year

    idade = data_atual - idade_atual
    if idade <= 18:
        return f'com {idade} anos: NAO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: VOTO OPCIONAL'
    else:
        return f'com {idade} anos: VOTO OBRIGATORIO'


idade_atual = int(input('informe que ano vc nasceu:'))
print(voto(idade_atual))
