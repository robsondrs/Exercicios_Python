fra = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} na frase'.format(fra.count('A')))
print('A primeira letra "A" aparece na posição {}'.format(fra.find('A') + 1))
print('A última letra "A" aparece na posição {}'.format(fra.rfind('A') + 1))