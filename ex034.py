sal = float(input('Qual é o salário do funcionário? R$'))
if sal > 1250:
    novo = sal * 1.1
else:
    novo = sal * 1.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, novo))

