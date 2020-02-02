jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
for c in range(0, jogos):
    jogador['gols'].append(int(input(f'   Quantos gols na partida {c+1}: ')))
jogador['total'] = sum(jogador['gols'])
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
