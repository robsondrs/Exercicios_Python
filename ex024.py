cidade = str(input('Em que cidade você nasceu? ')).strip()
print('O nome desta cidade começa com "Santo": {}'.format('santo' in cidade.split()[0].lower()))
# print(cidade[:5].upper() == 'SANTO')
