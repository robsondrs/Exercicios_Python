lista = []
jogador = dict()
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    jogador['total'] = 0
    for c in range(0, jogos):
        jogador['gols'].append(int(input(f'   Quantos gols na partida {c+1}: ')))
        jogador['total'] = sum(jogador['gols'])
    lista.append(jogador.copy())
    while True:
        cont = str(input('Quer continuar? [S/N] ')).upper()[0]
        if cont in 'SN':
            break
    if cont in 'N':
        break
print('-='*30)
print(f'{"Nº":<3}{"Jogador":<15}{"Gols":<15}{"Total":<15}')
print('-' * 40)
for k, v in enumerate(lista):
    print(f'{k:<3}', end='')
    for j in v.values():
        print(f'{str(j):<15}', end='')
    print()
print('-' * 40)
while True:
    opcao = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opcao == 999:
        break
    elif opcao >= len(lista):
        print('ERRO! Não existe este jogador.')
    else:
        print(f' -- Levantamento do jogador {lista[opcao]["nome"]}:')
        for i, v in enumerate(lista[opcao]['gols']):
            print(f'    No jogo {i+1} fez {v} gols.')
    print('-' * 40)
print('<< ENCERRADO >>')
