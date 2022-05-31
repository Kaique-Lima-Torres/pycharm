peso = float(input('qual o seu peso? (kg)?'))
altura = float(input('qual a sua altura? (m)'))
imc = peso / (altura * altura)
print(f'o seu imc e {imc:.2f}')
if imc < 18.5:
    print('voce esta abaixo do peso')
elif 18.5 <= imc <= 25:
    print('o seu peso e ideal')
elif 25 <= imc <= 30:
    print('voce tem sobrepeso')
elif 30 <= imc <= 40:
    print('voce esta na obesidade')
else:
    print('voce esta na obesidade morbida')
