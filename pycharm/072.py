nome_numero = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'trese', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezeonve', 'vinte'
while True:
    numeros = int(input('Digite um numero entre 0 e 20 para a sua leitura:'))
    if numeros < 0 or numeros > 20:
        print('numero invalido')
    else:
        print(f'vc digitou {nome_numero[numeros]}')
    resposta = str(input('voce quer continuar: [S/N]')).upper().strip()[0]
    if resposta == 'N':
        break
print('finalizando programa')

