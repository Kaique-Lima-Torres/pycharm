def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!digite novamente\033[m')
        except ZeroDivisionError:
            print('\033[0;31mERRO!DIGITE NOVAMENTE\033[m')

        except KeyboardInterrupt:
            print('\033[0;31mERRO!DIGITE NOVAMENTE\033[m')
        else:
            return n


num = leiaint('digite o primeiro valor:')
num_dois = leiaint('digite o segundo valor:')
print(f'o primeiro valor digitado foi {num}\ne o segundo valor foi {num_dois}\na soma deu {num + num_dois}')
