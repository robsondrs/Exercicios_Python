print('====== LOJAS SOARES ======')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA CARTÃO
[ 3 ] 2x NO CARTÃO
[ 4 ] 3x OU MAIS NO CARTÃO''')
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    ajuste = preco - preco * 10 / 100
elif opcao ==2:
    ajuste = preco - preco * 5 / 100
elif opcao == 3:
    ajuste = preco
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(preco / 2))
elif opcao == 4:
    ajuste = preco + preco * 20 / 100
    parcela = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, ajuste / parcela))
else:
    print('Opção inválida, tente novamente!')
    ajuste = preco
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, ajuste))
