palavras = ('aprender', 'python', 'tuplas', 'vogais', 'teclado', 'monitor', 'celular',
            'teste', 'mezanino', 'secretaria', 'papel', 'ponte', 'telefone', 'carimbo')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=" ")
