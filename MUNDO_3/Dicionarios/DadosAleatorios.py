from random import randint
from time import sleep

data:list = []

print('Valores sorteados: ')
for c in range(4):
    jogador:dict = {
        'Nome': c,
        'Jogada': randint(1, 6)
    }

    data.append(jogador)

for i in data:
    sleep(1)
    print('O Jogador{} tirou {}' .format(i['Nome'] + 1, i['Jogada']))

print('Ranking dos jogadores: ')


