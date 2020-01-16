times = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico - PR',
         'São Paulo','Internacional','Corinthians','Fortaleza',
         'Goiás','Bahia','Vasco','Atlético - MG','Fluminense',
         'Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avaí')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense esta na {times.index("Chapecoense") +1}ª posição')
