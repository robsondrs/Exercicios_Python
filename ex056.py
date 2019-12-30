media = 0
homem = ''
homemida = 0
mulher = 0
for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Nome: ')).strip().upper().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    media += idade
    if sexo in 'Mm' and idade > homemida:
        homem = nome
        homemida = idade
    elif sexo in 'Ff' and idade < 20:
        mulher += 1
print('A média de idade deste grupo de pessoas é {:.1f}.'.format(media / 4))
print('O homem mais velho do grupo tem {} anos e seu nome é {}.'.format(homemida, homem))
print('No grupo há {} mulheres com menos de 20 anos.'.format(mulher))
