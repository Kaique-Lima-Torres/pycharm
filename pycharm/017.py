from math import hypot

cosceno = float(input('comprimento do cateto oposto:'))
cateto = float(input('comprimento do cateto adjacente'))
hipotenusa = hypot(cosceno, cateto)
print(f'a hipotenusa vai medir {hipotenusa:.2f}')
