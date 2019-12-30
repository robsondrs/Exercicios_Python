n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
maior = n1 if n1 > n2 and n3 else n2 if n2 > n3 else n3
menor = n1 if n1 < n2 and n3 else n2 if n2 < n3 else n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

