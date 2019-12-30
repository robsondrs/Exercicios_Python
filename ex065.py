continuar = 'S'
cont = soma = maior = menor = 0
while continuar == 'S':
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    cont += 1
    soma += num
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('Você digitou {} números e a média foi {:.1f}'.format(cont, soma / cont))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
