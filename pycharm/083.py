expressao = str(input('digite sua expressao:'))
if expressao.count('(') == expressao.count(')'):
    print('expressao valida')
else:
    print('sua expressao ta errada, por favor digite de novo')
