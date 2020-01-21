lista = []
for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > max(lista):
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        for p in range(0, len(lista)):
            if valor <= lista[p]:
                lista.insert(p, valor)
                print(f'Valor adicionado na posição {p} da lista')
                break
print('-='*20)
print(f'Os valores digitados em ordem foram {lista}')
