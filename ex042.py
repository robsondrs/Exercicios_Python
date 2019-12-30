print('-=-'*9, '\nAnalisador de Triângilos\n' + '-=-'*9)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    res = 'PODEM FORMAR'
    if n1 == n2 == n3:
        tipo = 'EQUILÁTERO'
    elif n1 != n2 != n3 != n1:
        tipo = 'ESCALENO'
    else:
        tipo = 'ISÓSCELES'
else:
    res = 'NÃO PODEM FORMAR'
    tipo = ''
print('Os segmentos acima {} um triângulo {}.'.format(res, tipo))
