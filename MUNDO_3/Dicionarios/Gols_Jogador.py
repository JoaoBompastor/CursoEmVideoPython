gols:list = []

nome = str(input('Qual é o nome do jogador? ')).strip() .capitalize()
partidas = int(input(f'Quantas partidas {nome} jogou? '))
total = 0

for c in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))

print('-=-' * 20)

for gol in gols:
    total += gol

Jogador:dict = {
    'Nome': nome,
    'Gols': gols,
    'Total': total
}
print(Jogador)

print('-=-' * 20)

for key, value in Jogador.items():
    print(f'O campo {key} tem o valor {value}')

print('-=-' * 20)

print(f'O jogador {nome} jogou {partidas} partidas.')

for p, g in enumerate(gols):
    print(f'    => Na partida {p}, ele fez {g} gols.')

print(f'Foi um total de {total} gols.')