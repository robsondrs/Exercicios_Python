lista = ('Pão',1.89,'Queijo',20.99,'Presunto',17.99,'Leite',2.89,'Carne',25.57,'Arroz',5.00,
         'Feijão',7.89,'Vassoura',8.99,'Lentilha',5.57,'Bombom',0.99)
print('-='*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-='*20)
for pos, item in enumerate(lista):
    if pos % 2 == 0:
        print(f'{item:.<32}R${lista[pos+1]:>6.2f}')
print('-='*20)
