lista = []
PosicaoMaior = []
PosicaoMenor = []


for numeros in range(5):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

for posicao in range (0, len(lista)):
    if lista[posicao] == max(lista):
        PosicaoMaior.append(posicao + 1)

    elif lista[posicao] == min(lista):
        PosicaoMenor.append(posicao + 1)

print(f'Voce digitou os valores: {lista}')
print(f'O maior valor digitado foi o valor {max(lista)}, e ele apareceu nas posicoes {PosicaoMaior}')
print(f'O menor valor digitado foi o valor {min(lista)}, e ele apareceu nas posicoes {PosicaoMenor}')