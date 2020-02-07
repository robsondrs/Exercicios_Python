from time import sleep

cores = ('\033[m',  # 0 - sem cor
     '\033[30:41m',  # 1 - vermelho
     '\033[30:42m',  # 2 - verde
     '\033[30:43m',  # 3 - amarelo
     '\033[30:44m',  # 4 - azul
     '\033[30:45m',  # 5 - roxo
     '\033[7;30m'  # 6 - branco
     )


def cor(n):
    print(cores[n], end='')


def printForm(txt, c=0):
    cor(c)
    print(f'~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))
    cor(0)


while True:
    printForm('SISTEMA DE AJUDA PyHELP', 2)
    h = input('Função ou Biblioteca > ').strip()
    if h.upper() == 'FIM':
        break
    printForm(f'Acessando o manual do comando \'{h.upper()}\'', 4)
    sleep(1.5)
    cor(6)
    help(h)
    sleep(2)
    cor(0)
printForm('ATÉ LOGO', 1)
