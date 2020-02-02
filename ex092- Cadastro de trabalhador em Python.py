from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
anoAtual = datetime.now().year
trabalhador['idade'] = anoAtual - int(input('Ano de Nascimento: '))
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + 35 - (anoAtual - trabalhador['contratacao'])
print('-='*20)
for k, v in trabalhador.items():
    print(f'   - {k} tem o valor {v}')
