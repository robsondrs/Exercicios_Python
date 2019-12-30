soma = cont =0
while True:
    num = int(input('Digite um valor: [999 p/ parar] '))
    if num == 999:
        break
    soma += num
    cont += 1
print('Voce digitou {} e a soma é {}'.format(cont, soma))
