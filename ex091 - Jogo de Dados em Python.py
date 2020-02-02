from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
ranking = list()
for c in range(1, 5):
    jogo[f'jogador{c}'] = randint(1, 6)
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-='*20)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
