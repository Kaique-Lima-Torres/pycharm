soma = 0
acum = 0
for c in range(1, 501, 2):  # o numero 2 mostra numeros inpares
    if c % 3 == 0:  # se o c for divisivel por 3
        soma += c  # vai fazer um acumulo e fazer a soma a multiplicacao entre os numeros comecando do 0 e terminando no c
        acum += 1  # ele conta +1 fazendo a soma
print(f'a soma de todos os {acum} valores deu {soma}')
