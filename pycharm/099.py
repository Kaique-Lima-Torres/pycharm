def maior(*lista):
    print('*-*'*30)
    print('analisando os valores passandos...')
    print(f'{lista} foram informados {len(lista)} valores ao todo')
    print(f'o maior valor informado foi {max(lista)}')



maior(7, 8, 0, 3, 2, 5)
maior(8, 10, 6)
maior(4)
maior(17, 28, 21, 78)
maior(100, 83, 48, 53, 1)