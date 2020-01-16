extenso = ('zero','um','dois','três','quatro',
           'cinco','seis','sete','oito','nove',
           'dez','onze','doze','treze','catorze',
           'quinze','dezesseis','dezessete',
           'dezoito','dezenove','vinte')
while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente. ',end='')
    print(f'Você digitou o número {extenso[numero]}.')
    while True:
        continuar = input('Deseja continuar [S/N]: ').upper()
        if continuar[0] in 'SN':
            break
    if continuar == 'N':
        break
print('Fim do programa.')