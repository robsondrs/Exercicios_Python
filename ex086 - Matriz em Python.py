matriz = [[], [], []]
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {i}]: ')))
print('-='*30)
for l in range(0, len(matriz)):
    for n in range(0, len(matriz[l])):
        print(f'[{matriz[l][n]:^5}]', end='')
    print()
