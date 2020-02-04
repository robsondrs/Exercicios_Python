def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')


print(' Controle de Terreno')
print('---------------------')
largura = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(largura, comp)
