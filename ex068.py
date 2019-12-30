from random import randint
print('-=' * 13)
print('VAMOS JOGAR PAR OU IMPAR')
cont = 0
while True:
    print('-=' * 13)
    jogador = int(input('Digite um valor: '))
    while True:
        jogada = str(input('PAR ou IMPAR [P/I]: ')).strip().upper()[0]
        if jogada in 'PI':
            break
    computador = randint(0, 10)
    total = jogador + computador
    resultado = 'PAR' if total % 2 == 0 else 'IMPAR'
    print('-' * 26)
    print('Você jogou {} e o computador {}. Total de {} deu {}.'.format(jogador, computador, total, resultado))
    print('-' * 26)
    if jogada == resultado[0]:
        print('Você VENCEU...')
        print('Vamos jogar novamente.')
        cont += 1
    else:
        print('Você PERDEU...')
        break
print('-=' * 13)
print('GAME OVER!!! Você venceu {} vezes.'.format(cont))
