reta1 = float(input('Qual o comprimento da primeira reta?'))
reta2 = float(input('Qual o comprimento da segunda reta?'))
reta3 = float(input('Qual o comprimento da terceira reta?'))
if reta1 == reta2 and reta1 == reta3:
    print('os seguimentos acima podem formar um triangulo EQUILATERO')
elif reta1 == reta2 or reta1 == reta3 or reta2 == reta2:
    print('os seguimentos acima podem formar um triangulo ISOSCELES')
elif reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('os seguimentos acima podem formar um triangulo ESCALENO')
else:
    print('os seguimentos acima nao podem formar um triangulo')
