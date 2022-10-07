# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Flamengo

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico PR', 'Atlético MG',
        'América MG', 'Botafogo', 'São Paulo', 'Fortaleza', 'Bragantino', 'Góias', 'Santos', 'Ceará', 'Coritiba', 
        'Cuiabá', 'Atlético GO', 'Avaí', 'Juventude')
print(f'Os times do Brasileirão 2022 são: {times}.')
print(f'Os cinco primeiros colocados são {times[:5]}')
print(f'Os últimos 4 colocados são {times[16:]}')
print(f'O Flamengo está na posição {times.index("Flamengo") + 1}° posição')