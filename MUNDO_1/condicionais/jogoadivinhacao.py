from random import randint

Ncomputador = randint(0, 5)
print('-=-' *20)
print('eu pensei em um numero entre 0 e 5, tente adivinhar...')
print('-=-' *20)

tentativa = int(input('tente adivinhar o numero: '))

if(tentativa == Ncomputador):
    print('acertou!')

else:
    print('perdeu! eu pensei no numero {}' .format(Ncomputador))