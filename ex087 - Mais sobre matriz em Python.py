matriz = [[], [], []]
sPares = sTerceiraC = mSegundaL = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite o valor para [{l}, {c}]: ')))
print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
        if matriz[l][c] % 2 == 0:
            sPares += matriz[l][c]
        if c == 2:
            sTerceiraC += matriz[l][c]
        if l == 1:
            if c == 0 or matriz[l][c] > mSegundaL:
                mSegundaL = matriz[l][c]
    print()
print('-='*20)
print(f'A soma dos valores pares é {sPares}')
print(f'A soma dos valores da terceira coluna é {sTerceiraC}')
print(f'O maior valor da segunda linha é {mSegundaL}')
