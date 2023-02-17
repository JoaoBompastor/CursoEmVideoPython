brasileirao_2022 = (
    "Flamengo",
    "Santos",
    "Palmeiras",
    "Internacional",
    "Atlético-MG",
    "São Paulo",
    "Athletico-PR",
    "Corinthians",
    "Grêmio",
    "Ceará",
    "Bahia",
    "Fluminense",
    "Fortaleza",
    "Red Bull Bragantino",
    "Vasco da Gama",
    "Corinthians-AL",
    "Goiás",
    "Botafogo",
    "Cuiabá",
    "Sport"
)

print('=' * 40)

print(f'A lista de times do brasileirão são:\n {brasileirao_2022}')

print('=' * 40)

print(f'Os 5 primeiros colocados foram:\n {brasileirao_2022[:5]}')

print('=' * 40)

print(f'Os ultimos 4 colocados foram:\n {brasileirao_2022[-4:]}')

print('=' * 40)

print(f'Times em ordem alfabetica:\n {sorted(brasileirao_2022)}')

print('=' * 40)

print('KKKKKKKKK O SPORT TA NA COLOCACAO {} KKKKKKKKKKK' .format(brasileirao_2022.index('Sport') + 1))
