from random import randint

jogos:list = []
jogo:list = []

#coletar a quantidade de jogos a serem criados
Quantidade_de_jogos = int(input('Quantos jogos deseja gerar? '))

#gerar jogos
for c in range(Quantidade_de_jogos):
    jogo.append(randint(0, 60))

    for i in range(5):
        if i != randint(0, 60):
            jogo.append(randint(0, 60))

    jogos.append(sorted(jogo[:])) 
    jogo.clear()

#printando bonitinho :)
for j in range(len(jogos)):
    print(f'Jogo {j + 1}:  {jogos[j]}')