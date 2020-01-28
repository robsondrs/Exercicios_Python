lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('-='*20)
print('Nº. NOME        MÉDIA')
print('-'*24)
for c, aluno in enumerate(lista):
    print(f'{c:<4}{aluno[0]:<12}{aluno[2]:>5.1f}')
while True:
    print('-' * 30)
    aluno = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    if aluno <= len(lista)-1:
        print(f'Notas de {lista[aluno][0]} são {lista[aluno][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
