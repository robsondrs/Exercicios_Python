from random import randint
sorteio = randint(0, 10)
quant_tent = 0
acertou = False
print('''Olá, sou seu computador...
Acabei de pensar em número de 0 a 10.
Será que você consegue adivinhar qual foi?''')
while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    quant_tent += 1
    if palpite < sorteio:
        print('Mais... Tente mais uma vez.')
    elif palpite > sorteio:
        print('Menos... Tente mais uma vez.')
    else:
        acertou = True
if quant_tent == 1:
    print('PARABÉNS!!!! Você acertou na primeira tentativa.')
else:
    print('Acertou com {} tentativas. PARABÉNS!!!'.format(quant_tent))
