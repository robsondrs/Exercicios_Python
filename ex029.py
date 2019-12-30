vel = float(input('Qual a velocidade do carro: '))
if vel <= 80:
    print('Tenha um bom dia! Dirija com segurança')
else:
    print('MULTADO! Você excedeu o limite permitido de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format((vel-80)*7))
