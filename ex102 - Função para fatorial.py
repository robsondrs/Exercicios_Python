def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um numero
    :param num: O numero a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número n.
    """
    print('-'*25)
    f = 1
    s = ''
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end=' ')
            if c != 1:
                print('x ', end='')
            else:
                print('= ', end='')
    return f


#PROGRAMA PRINCIPAL
print(fatorial(5, True))
