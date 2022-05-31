nota1 = float(input('digite a primeira nota:'))
nota2 = float(input('digite a segunda nota'))
media = (nota1 + nota2) / 2
print(f'a media do aluno e {media}')
if 7 > media >= 5:
    print('o aluno esta em RECUPERACAO')
elif media < 5:
    print('o aluno esta REPROVADO')
elif media >= 7:
    print('o aluno esta APROVADO')
