expressao = str(input('Digite a expressao: '))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simb)
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão esta errada!')


