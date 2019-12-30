from time import sleep
from random import randint
comp = randint(0, 2)
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
if -1 < jogador <=2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(0.5)
    print('-='*10)
    print('''COMPUTADOR JOGOU {}
JOGADOR JOGOU {}'''.format(jokenpo[comp], jokenpo[jogador]))
    print('-='*10)
    if jogador == 0 and comp == 2 or jogador == 1 and comp == 0 or jogador == 2 and comp == 1:
        print('JOGADOR VENCE')
    elif jogador == comp:
        print('HOUVE EMPATE')
    else:
        print('COMPUTADOR VENCE')
else:
    print('JOGADA INVÁLIDA')