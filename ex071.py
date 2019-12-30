print('=' * 30 + '\n           BANCO CEV\n' + '=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
notas = [50, 20, 10, 1]
ced = cont = 0
while True:
    if valor // notas[cont] != 0:
        ced = valor // notas[cont]
        print('Total de {} cédulas de R${:.2f}'.format(int(ced), notas[cont]))
        valor = valor % notas[cont]
    cont += 1
    if valor == 0:
        break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um Bom dia!')
