from time import sleep


def maior(*valores):
    print('-='*20)
    print('Analisando os valores passados')
    for v in valores:
        print(v, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(valores)} valores ao todo.')
    if len(valores) != 0:
        maior = max(valores)
    else:
        maior = 0
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
