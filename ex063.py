print('-' * 25)
print('  SEQUÊNCIA DE FIBONACCI')
print('-' * 25)
xtermos = int(input('Quantos termos você quer mostrar? '))
print('~' * 25)
cont = 1
termoad = termo = termopos = 0
while cont <= xtermos:
    print('{} -> '.format(termopos), end='')
    if termo == 0:
        termo += 1
        termopos += 1
    else:
        termopos = termo + termoad
        termoad = termo
        termo = termopos
    cont += 1
print('FIM')
print('~' * 25)
