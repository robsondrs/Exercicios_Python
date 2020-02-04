from random import randint
from time import sleep


def sortear(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lista.append(randint(0, 10))
        sleep(0.3)
        print(lista[i], end=' ')
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores {lista}, temos {soma}')


lst = []
sortear(lst)
somaPar(lst)
