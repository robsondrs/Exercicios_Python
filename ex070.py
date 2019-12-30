print('-' * 30)
print('        LOJAS SOARES')
print('-' * 30)
total = menor = maismil = 0
nomememor = ''
while True:
    nome = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    if total == 0 or preco < menor:
        menor = preco
        nomememor = nome
    if preco > 1000:
        maismil += 1
    total += preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi R${:.2f}'.format(total))
print('Temos {} produtos que custando mais de R$1000,00'.format(maismil))
print('O produto mais barato foi {} que custa R${:.2f}'.format(nomememor, menor))
