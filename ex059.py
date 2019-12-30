from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção: '))
    if opcao == 1:
        print('A soma entre {} + {} é {}.'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('O resultado de {} x {} é {}.'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('Entre {0} e {1} o maior valor é {0}.'.format(num1, num2))
        elif num2 > num1:
            print('Entre {0} e {1} o maior valor é {1}.'.format(num1, num2))
        else:
            print('Os dois valores são iguais a {}.'.format(num1))
    elif opcao == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-='*15)
    sleep(2)
print('Fim do programa! Volte sempre!')
