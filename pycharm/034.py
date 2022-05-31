salario = float(input('qual e o salario do funcionario?'))
novo_salario = salario * 1.10
if salario >= 1250:
    print(f'quem ganhava R${salario:.2f} com 10% de reajuste ganhara R${novo_salario:.2f}')
else:
    print(f'quem ganhava {salario:.2f} com 15% de reajuste ganhara {salario * 1.15:.2f}')
