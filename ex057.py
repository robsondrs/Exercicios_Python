sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while not sexo in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip()
print('Sexo {} cadastrado com sucesso.'.format(sexo.upper()))
