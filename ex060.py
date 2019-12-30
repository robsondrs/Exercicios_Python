fatorial = num = dresc_fat = int(input('''Escolha um número para
calcular seu fatorial:'''))
ord_fat = ''
while dresc_fat != 0:
    ord_fat += str(dresc_fat)
    if dresc_fat != 1:
        ord_fat += ' x '
    if fatorial != dresc_fat:
        fatorial *= dresc_fat
    dresc_fat -= 1
print('Calculando {}! = {} = {}'.format(num, ord_fat, fatorial))
