from math import radians, sin, cos, tan

angulo = float(input('dogote o angulo desejado:'))
seno = sin(radians(angulo))
print(f'o seno sera de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'o cosseno sera de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'a tangente sera de {tangente:.2f}')
