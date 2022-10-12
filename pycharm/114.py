import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('o site nao ta disponivel')
else:
    print('consegui acessar o site')