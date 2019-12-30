while True:
    num = int(input('Digite um número para ver a tabuada: '))
    print('-' * 40)
    if num < 0:
        break
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(num, c, num * c))
    print('-' * 40)
print('GERADOR DE TABUADA ENCERRADO. Volte sempre!')
