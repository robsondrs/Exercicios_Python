from datetime import date
ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
anoalis = anoatual + (18 - idade)
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, anoatual))
if idade < 18:
    print('''Ainda faltam {} anos para o alistamento
Seu alistamento será em {}.'''.format(18 - idade, anoalis))
elif idade > 18:
    print('''Você já deveria ter se alistado há {} anos
Seu alistamento foi em {}.'''.format(idade - 18, anoalis))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')

