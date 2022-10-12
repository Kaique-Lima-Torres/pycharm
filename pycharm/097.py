def frase(txt):
    tamanho = len(txt) + 4
    print('-'*(tamanho))
    print(f'{txt.center(tamanho)}')
    print('-'*(tamanho))


txt = str(input('escreva sua frase:'))
print(frase(txt=txt))