peso = float(input('Qual é seu peso? (Kg) '))
alt = float(input('Qual é sua altura? (m) '))
imc = peso / alt ** 2
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO DO PESO normal.')
elif imc < 25:
    print('Parabéns, você esta na faixa de PESO NORMAL.')
elif imc < 30:
    print('Você esta com SOBREPESO.')
elif imc < 40:
    print('Você esta em OBESIDADE.')
elif imc >= 40:
    print('Você está em OBESIDADE MORBIDA, cuidado!.')
