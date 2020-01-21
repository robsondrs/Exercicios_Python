lista = []
resposta = 'S'
while resposta == 'S':
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        resposta = input('Quer continuar? [S/N] ').upper().strip()[0]
        if resposta[0].upper() in 'SN':
            break
print('-='*20)
print(f'Voce digitou os valores {sorted(lista)}')