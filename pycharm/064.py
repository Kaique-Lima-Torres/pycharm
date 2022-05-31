n = total = cont = 0
while n != 999:
    n = int(input('digite um numero [999 para parar]:'))
    if n != 999:
        total += n
        cont += 1
print(f'vc digitou {cont} e somando deu {total}')
