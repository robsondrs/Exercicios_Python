extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numero = int(input('Digite um número entre 0 e 20: '))
while True:
    if numero >= 0 and numero <= 20:
        break
    numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[numero]}.')
