# obj: criar um programa que identifica palavras em uma lista e printa suas letras.

lista = []


#loop base para obter as palavras.
while True:
    palavra = str(input('Digite uma palavra: ')).strip() .capitalize()

    lista.append(palavra)

    continuar = str(input('Deseja continuar? [s/n] ')).strip() .upper()[0]

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [s/n] ')).strip() .upper()[0]

