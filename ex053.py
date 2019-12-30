frase = str(input('Digite uma frase: ')).strip().upper().replace(' ','')
nfrase = ''
for c in range(len(frase)-1, -1, -1):
    nfrase += frase[c]
print('O inverso de {} é {}'.format(frase, nfrase))
if frase == nfrase:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
