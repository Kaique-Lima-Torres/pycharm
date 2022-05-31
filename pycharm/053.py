frase = str(input('digite uma frase:')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('e um palindromo')
else:
    print('nao e um palindromo')
