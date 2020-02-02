lista = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO! Por Favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        cont = str(input('Quer continuar? [S/N] ')).upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Responda apenas S OU N.')
    if cont in 'N':
        break
print('-='*30)
media = soma / len(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for i in range(0, len(lista)):
    if lista[i]['sexo'] == 'F':
        print(lista[i]['nome'], end=' ')
print()
print(f'D) A lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] > media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
