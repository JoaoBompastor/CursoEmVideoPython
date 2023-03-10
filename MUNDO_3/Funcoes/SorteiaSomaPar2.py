from random import randint
from time import sleep

class program:
    """
    -> programa contendo duas funcoes, uma sorteia 5 numeros aleatorios em uma lista, e a outra
        soma os numeros pares dessa lista
    """

    @staticmethod
    def sorteia(lista:list) -> list:
        for c in range(5):
            random_integer:int = randint(1, 10)
            print(random_integer, end=' ', flush= True)
            lista.append(random_integer)
            sleep(0.3)

        print('Done!')
        print(f'Lista: {numeros}')

    @staticmethod
    def somapar(lista:list) -> list:
        pares = [p for p in numeros if p % 2 == 0]

        print(f'Soma dos numeros pares da lista: {sum(pares)}')


numeros:list = []
run = program()

run.sorteia(numeros)
run.somapar(numeros)

help(program)