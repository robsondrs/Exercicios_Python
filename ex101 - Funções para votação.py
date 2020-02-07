def voto(anoNasc):
    from datetime import date
    idade = date.now().year - anoNasc
    voto = f'Com {idade} anos: '
    if 16 <= idade < 18 or idade > 65:
        voto += "VOTO OPCIONAL"
    elif 18 <= idade <= 65:
        voto += "VOTO OBRIGATÓRIO"
    else:
        voto += "NÃO VOTA"
    return voto


print('-'*25)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
