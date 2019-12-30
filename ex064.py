cont = soma = num = 0
while num != 999:
    num = int(input('Digite um número [999 p/ parar]: '))
    if num != 999:
        cont += 1
        soma += num
print('Você digitou {} números e a soma deles é {}.'.format(cont, soma))
