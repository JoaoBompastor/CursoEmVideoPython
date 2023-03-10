from random import randint
import time

def sorteia():
    print('sorteando os numeros da lista: ', end=' ')

    for c in range(5):
        numero = randint(0, 10)
        print(numero, end=' ', flush= True)
        numeros.append(numero)
        time.sleep(0.3)

    print('PRONTO!')

def somapar(lista:list):
    somapares = 0

    for c in lista:
        if c % 2 == 0:
            somapares += c
    
    print(f'\nsomando os valores pares de {lista} temos: {somapares}')


numeros:list = []

sorteia()
somapar(numeros)