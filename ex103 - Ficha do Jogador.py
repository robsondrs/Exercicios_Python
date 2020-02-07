def ficha(nome='<Desconhecido>', gols=0):
    """
    -> Mostra a ficha de um Jogador
    :param nome: Nome do jogador
    :param gols: Total de Gols
    :return: Sem retorno
    """
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# programa Principal
j = str(input('Nome do Jogador: ')).strip()
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j == '':
    ficha(gols=g)
else:
    ficha(n, g)
