from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade <= 9:
    classi = 'MIRIM'
elif idade <= 14:
    classi = 'INFANTIL'
elif idade <= 19:
    classi = 'JÚNIOR'
elif idade <= 25:
    classi = 'SÊNIOR'
elif idade > 25:
    classi = 'MASTER'
print('''O atleta tem {} ano(s).
Classificação: {}'''.format(idade, classi))
