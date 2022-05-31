import time

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
time.sleep(1)
print(f'Seu nome completo em maiusculas é {nome.upper()}')
print(f'Seu nome completo em minusculas é {nome.lower()}')
espacos = (nome.count(' '))
print(f'Seu nome tem ao todo {len(nome) - espacos} letras')
primeiro = nome.find(' ')
print(f'Seu primeiro nome tem {primeiro} letras.')
