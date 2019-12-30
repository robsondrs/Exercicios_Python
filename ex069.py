cont18 = homens = mulheres = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('IDADE: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if idade >= 18:
        cont18 += 1
    print('-' * 30)
    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('Total de pessoas com mais de 18 anos: {}'.format(cont18))
print('Ao todo temos {} homens cadastrados.'. format(homens))
print('E temos {} mulheres com menos de 20 anos.'.format(mulheres))
