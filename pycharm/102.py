def fatorial(n, show=False):
    """
    ->programa que ve o fatorial
    :param n: numero
    :param show: True or False
    :return: retorna o f
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f


n = int(input('digite um numero:'))
print(fatorial(5, show=False))
