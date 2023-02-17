from random import randint

tupla = (
    int(input('Digite um numero: ')),
    int(input('Digite outro numero: ')),
    int(input('Digite mais um numero: ')),
    int(input('Digite o ultimo numero: '))
)

print(f'Voce digitou os valores {tupla}')

print(f'O valor 9 apareceu {tupla.count(9)}')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posicao.')

else:
    print('O valor 3 nao foi digitado.')

print('Os valores pares digitados foram: ', end='')

for numeros in tupla:
    if numeros % 2 == 0:
        print(numeros, end=' ')