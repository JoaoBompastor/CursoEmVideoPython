from random import randint

count = soma = 0

while True:
    print('-=-' * 20)
    print('VAMOS JOGAR PAR OU IMPAR?')
    print('-=-' * 20)

    computador = randint(1, 10)
    jogador = int(input('Sua jogada: '))
    escolha = str(input('Par ou Impar? [P/I] ')).strip() .upper()[0]
    soma = computador + jogador

    if soma % 2 == 0:
        print(f'Voce jogou {jogador} e o computador jogou {computador}, o total {soma} DEU PAR')

    elif soma % 2 == 1:
        print(f'Voce jogou {jogador}, o computador jogou {computador} e o total {soma} DEU IMPAR')

    if escolha == 'P':
        if soma % 2 == 0:
            print('Voce ganhou!')
            print('Vamos jogar novamente...')
            count += 1
        
        else:
            print('Voce perdeu...')
            break
    
    if escolha == 'I':
        if soma % 2 == 0:
            print('Voce perdeu...')
            break

        else:
            print('Voce ganhou!')
            print('Vamos jogar novamente...')
            count += 1

print(f'Voce ficou invicto por {count} rodadas!')