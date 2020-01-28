lista = list()
maior = menor = 0
while True:
    lista.append([str(input('Nome: ')),
                  float(input('Peso: '))])
    continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar in 'N':
        break
print('-='*30)
print(f'Ao todo, você cadastou {len(lista)} pessoas.')
for p in range(0,len(lista)):
    if p == 0:
        maior = menor = lista[0][1]
    elif lista[p][1] > maior:
        maior = lista[p][1]
    elif lista[p][1] < menor:
        menor = lista[p][1]
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor:.1f}Kg. peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
