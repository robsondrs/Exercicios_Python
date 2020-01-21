lista = []
resposta = 'S'
while resposta == 'S':
    lista.append(int(input('Digite um valor: ')))
    while True:
        resposta = input('Quer continuar? [S/N] ').upper().strip()[0]
        if resposta in 'SN':
            break
print('-='*20)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)} ')
if 5 in lista:
    print('O valor 5 faz parte da lista e esta nas posições ', end='')
    for pos, item in enumerate(lista):
        if 5 == item:
            print(pos, end='... ')
else:
    print('O valor 5 não faz parte da lista!')
