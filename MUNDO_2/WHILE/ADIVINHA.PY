from random import randint

contador = 1
computador = randint (0, 10)
jogador = int(input('tente adivinhar o numero que o computador escolheu: '))

while jogador != computador:

    if jogador > computador:
        jogador = int(input('Menos... Continue tentando: '))
    
    else:
        jogador = int(input('Mais... Continue tentando: '))
 
    contador += 1

print('Voce acertou! o computador pensou no numero {}!' .format(computador))
print('voce levou {} tentativas para acertar!' .format(contador))