valores = []
for p in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {p}: ')))
print('=-'*30)
print(f'Você digitou os valoes {valores}')

print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == max(valores):
        print(f'{pos}...', end='')

print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == min(valores):
        print(f'{pos}...', end='')
