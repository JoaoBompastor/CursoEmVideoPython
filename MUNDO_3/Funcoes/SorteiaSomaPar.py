from random import randint

def sorteia():
    print('sorteando os numeros da lista: ', end=' ')

    for c in range(5):
        numero = randint(0, 10)
        print(numero, end=' ')
        numeros.append(numero)

def somapar(lista:list):
    somapares = 0

    for c in lista:
        if c % 2 == 0:
            somapares += c
    
    print(f'\nsomando os valores pares de {lista} temos: {somapares}')


numeros:list = []

sorteia()
somapar(numeros)