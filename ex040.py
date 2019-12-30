n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    resultado = 'APROVADO'
elif media >= 5 and media <=6.9:
    resultado = 'em RECUPERAÇÃO'
elif media <5:
    resultado = 'REPROVADO'
print('A média do aluno é {:.1f}'.format(media))
print('O aluno está {}.'.format(resultado))
