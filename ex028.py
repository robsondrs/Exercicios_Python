import random
from time import sleep
num = random.randint(0, 5)
print('-=-'*19)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5. TENTE ADIVINHAR...')
print('-=-'*19)
num1 = int(input('Em que numero eu pensei: '))
print('PROCESSANDO...')
sleep(3)
if num1 == num:
    print('PARABÉNS!!! Você conseguiu me vencer!')
else:
    print('GANHEI!!! Eu pensei no número {} e não no {}'.format(num, num1))
