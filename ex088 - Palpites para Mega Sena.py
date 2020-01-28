from random import randint
from time import sleep
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
palpites = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
for p in range(0, quant):
    palpites.append([])
    while len(palpites[p]) < 6:
        num = randint(1, 60)
        if num not in palpites[p]:
            palpites[p].append(num)
print(f'{"-="*3} SORTEANDO {quant} JOGOS {"-="*3}')
for c in range(0, quant):
    sleep(1)
    palpites[c].sort()
    print(f'Jogo {c+1}: {palpites[c]}')
print(f'{"="*8} < BOA SORTE > {"="*8}')
