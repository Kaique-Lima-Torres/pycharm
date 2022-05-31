numero = int(input('digite um numero inteiro:'))
print('''escolha uma das bases pra conversao:
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal''')
opcao = int(input('sua opcao:'))
if opcao == 1:
    print(f'{numero} convertido em binario fica {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para octal e igual a {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido em hexadecimal fica {hex(numero)[2:]}')
else:
    print('opcao invalida. tente novamente')
