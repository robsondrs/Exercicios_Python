from random import randint
sorteados = (randint(0,10),randint(0,10),randint(0,10),
             randint(0,10),randint(0,10))
maior = menor = sorteados[0]
print('Os valores sorteados foram: ', end="")
for numero in sorteados:
    print(numero, end=" ")
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'\nO maior numero sorteado foi {maior}')
print(f'O menor numero sorteado foi {menor}')

#solução mais simples para maior e menor
#print(f'\nO maior numero sorteado foi {max(sorteados}')
#print(f'O menor numero sorteado foi {min(sorteados}')
