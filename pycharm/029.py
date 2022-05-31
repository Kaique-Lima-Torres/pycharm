velocidade = int(input('qual a velocidade do seu carro?'))
multa = (velocidade-80) * 7
if velocidade > 80:
    print('\033[1;13mMULTADO\033[M! voce excedeu o limite permitido que e de 80km/h')
    print(f'voce deve pagar uma multa de {multa:.2f}')
else:
    print('Tenha um Bom dia, Diriga com seguranca')
