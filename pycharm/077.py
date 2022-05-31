frase = (
    'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO'
                                                                                                           'PROGRAMADOR',
    'FUTURO')
for p in frase:  # vai analisar cada elemento da tupla
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for frase in p:  # cada letra na palavra que ele pegou
        if frase.lower() in 'aeiou':  # analisar se essa letra ta dentro das vogais
            print(frase, end=' ')
