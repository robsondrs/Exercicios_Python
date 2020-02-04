from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 15)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo += 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    cont = inicio
    if cont < fim:
        while cont <= fim:
            print(cont, end=" ")
            sleep(0.5)
            cont += passo
    else:
        while cont >= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont -= passo
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 15)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
