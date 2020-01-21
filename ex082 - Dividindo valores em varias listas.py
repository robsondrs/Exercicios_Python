lista = []
impar = []
par = []
continuar = 'S'
while continuar == 'S':
    lista.append(int(input('Digite um valor: ')))
    while True:
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if continuar in 'SN':
            break
for num in lista:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print('-='*20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de imapres é {impar}')
