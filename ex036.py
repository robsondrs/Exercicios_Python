casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
pres = casa / (anos * 12)
por = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {}, a prestação será R${:.2f}'.format(casa, anos, pres))
if pres <= por:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
