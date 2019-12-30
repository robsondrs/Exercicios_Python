nome = str(input('Digite seu nome completo: ')).upper().strip()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu ultimo nome é {}'.format(nome.split()[len(nome.split())-1]))

# n = nome.split()  'divide em uma lista
# n[0]              'primeiro nome
# n[len(nome)-1]    'ultimo nome
