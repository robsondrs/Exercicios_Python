num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[036m{}\033[m'.format(c), end=' ')
        cont += 1
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
print('\nO número {} foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
    