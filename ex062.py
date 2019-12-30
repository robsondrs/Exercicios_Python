print('GERADOR DE PA')
print('-='*7)
termo = primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
xtermos = 10
total = 0
while xtermos != 0:
    total += xtermos
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    xtermos = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
