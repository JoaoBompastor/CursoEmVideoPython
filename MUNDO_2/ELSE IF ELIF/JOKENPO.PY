#jo ken po 1:pedra 2:papel 3:tesoura
from random import randint

PEDRA = 'PEDRA'
PAPEL = 'PAPEL'
TESOURA = 'TESOURA'

COMPUTADOR = randint(1, 3)

if COMPUTADOR == 1:
    ESCOLHA_COMPUTADOR = PEDRA

elif COMPUTADOR == 2:
    ESCOLHA_COMPUTADOR = PAPEL

elif COMPUTADOR == 3:
    ESCOLHA_COMPUTADOR = TESOURA

print('-=-' *20)
print('JO KEN PO!')
print('-=-' * 20)
print('''ESCOLHA UMA DAS OPCOES ABAIXO E DESAFIE O COMPUTADOR NUMA PARTIDA DE JO KEN PO!
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA

    [ 4 ] segredo...
''')
print('-=-' *20)

ESCOLHA = int(input('Digite sua escolha: '))
print('-=-' * 20)

if ESCOLHA == 1:
    NOVA_ESCOLHA = PEDRA

elif ESCOLHA == 2:
    NOVA_ESCOLHA = PAPEL

elif ESCOLHA == 3:
    NOVA_ESCOLHA = TESOURA

else:
    print('jogada invalida.')

#CHECANDO IGUAIS
if NOVA_ESCOLHA == ESCOLHA_COMPUTADOR:
    print('EMPATE!')

#GANHANDO
elif NOVA_ESCOLHA == PEDRA and ESCOLHA_COMPUTADOR == TESOURA:
    print('Voce ganhou!')

elif NOVA_ESCOLHA == PAPEL and ESCOLHA_COMPUTADOR == PEDRA:
    print('Voce ganhou!')

elif NOVA_ESCOLHA == TESOURA and ESCOLHA == PAPEL:
    print('Voce ganhou!')

#PERDENDO
elif NOVA_ESCOLHA == PEDRA and ESCOLHA_COMPUTADOR == PAPEL:
    print('Voce perdeu!')

elif NOVA_ESCOLHA == PAPEL and ESCOLHA_COMPUTADOR == TESOURA:
    print('Voce perdeu!')

elif NOVA_ESCOLHA == TESOURA and ESCOLHA_COMPUTADOR == PEDRA:
    print('Voce perdeu!')

#PRINTANDO BONITINHO
print('-=-' * 20)
print(F'''
SUA ESCOLHA: {NOVA_ESCOLHA}
ESCOLHA DO COMPUTADOR: {ESCOLHA_COMPUTADOR}
''')
print('-=-' * 20)