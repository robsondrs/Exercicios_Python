via = float(input('Qual a distancia de sua viagem: '))
print('Você esta prestes a começar uma viagem de {:.1f}Km.'.format(via))
if via <= 200:
    print('O preço de sua viagem será de R${:.2f}'.format(via * 0.5))
else:
    print('O preço de sua viagem será de R${:.2f}'.format(via * 0.45))
