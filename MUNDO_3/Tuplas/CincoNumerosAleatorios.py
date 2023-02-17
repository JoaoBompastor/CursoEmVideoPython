from random import randint

menor = 0
maior = 0

numero1 = randint(0, 10) 
numero2 = randint(0, 10)
numero3 = randint(0, 10)
numero4 = randint(0, 10)
numero5 = randint(0, 10)

tupla = (numero1, numero2, numero3, numero4, numero5)

for numeros in range(0, len(tupla)):
    if numeros == 0:
        menor = tupla[numeros]
        maior = tupla[numeros]

    if tupla[numeros] < menor:
        menor = tupla[numeros]
    
    if tupla[numeros] > maior:
        maior = tupla[numeros]

print(f'Tupla: {tupla}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
