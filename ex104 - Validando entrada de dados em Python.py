def leiaInt(txt):
    while True:
        num = str(input(txt))
        if num.isnumeric():
            return int(num)
        else:
            print('\033[1;31mERRO! Digite um número válido.\033[m')


# programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
