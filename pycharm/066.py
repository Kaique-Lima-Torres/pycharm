n = s = 1
acum = 0
while True:
    n = int(input('digite um numero para ver sua soma: digite [999] para parar o programa'))
    if n == 999:
        break
    s += n
    acum += 1
print(f'a soma dos {acum} vale {s}')
