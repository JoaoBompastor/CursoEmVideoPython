jogadores:list = []
gols:list = []
total:int = 0

# adicionar jogadores:

while True:
    nome = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {nome} jogou? '))

    for c in range(partidas):
        gol = int(input(f'Quantos gols na partida {c + 1}? '))
        total += gol
        gols.append(gol)

    jogador:dict = {
        'nome': nome,
        'gols': gols,
        'total': total
    }
    jogadores.append(jogador)

    continuar = str(input('Continuar? [S/N] ')).strip() .upper()[0]

    while continuar not in 'SN':
         continuar = str(input('Continuar? [S/N] ')).strip() .upper()[0]

    if continuar == 'N':
         break

# mostrar gols em partidas especificas:
while True:
    print('COD  NOME    GOLS    TOTAL')
    print('===' * 10)

    for count, e in enumerate(jogadores):
        print(count, end= ' ')

        for key, value in e.items():
            print(value, end=' ')
        
        print('\n')

    ver_jogador:int = int(input('Deseja analisar qual jogador? [999 flag] '))

    while ver_jogador != 999:
        while ver_jogador >= len(jogadores):
            ver_jogador:int = int(input('Opção inválida. Deseja analisar qual jogador? [999 flag] '))

        print('-- LEVANTAMENTO DO JOGADOR {}' .format(jogadores[ver_jogador]['nome']))

        for contagem, count in enumerate(jogadores[ver_jogador]['gols']):
            print(f'No jogo {contagem} fez {count} gols')
            contagem += 1

            if contagem == len(jogadores[ver_jogador]['gols']):
                ver_jogador:int = int(input('Deseja analisar qual jogador? [999 flag] '))

    else:
        break

print('FIM')
