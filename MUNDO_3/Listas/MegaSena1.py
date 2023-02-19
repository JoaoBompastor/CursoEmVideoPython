from random import randint

jogos:list = []
jogo:list = []

#funcao que gera os jogos
def Gerar_Jogo():
    jogo.append(randint(0, 60))

    for c in range(5):
        numero = randint(0, 60)

        if c != numero:
            jogo.append(numero)
        
        else: pass

Quantidade_de_jogos = int(input('Quantos jogos você quer gerar? '))

#loop que cria uma lista com o numero de jogos que o usuario deseja
for i in range(Quantidade_de_jogos):
    Gerar_Jogo()
    jogos.append(jogo[:])
    jogo.clear()

#print
for j in range(Quantidade_de_jogos):
    print(f'Jogo {j + 1}: {sorted(jogos[j])}')