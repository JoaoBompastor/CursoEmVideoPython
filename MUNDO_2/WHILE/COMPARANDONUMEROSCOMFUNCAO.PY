#parado pq nn sei mexer com funcao ainda:

maior = menor = count = soma = 0

numero = int(input('digite um numero: '))
choice = str(input('Deseja continuar? [S/N] ')).strip() .upper()
count += 1
soma += numero
list = []

def comparar(numero, maior, menor):
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

while choice == 'S':
    comparar(numero= numero, maior= maior, menor= menor)
    media = numero / count
    list.append(numero)
    numero = int(input('digite um numero: '))
    choice = str(input('Deseja continuar? [S/N] ')).strip() .upper()

    count += 1
    soma += numero

else:
    comparar(numero= numero, maior= maior, menor= menor)
    print('Voce digitou {} numeros, e a média deles foi: {}' .format(numero, media))
    print('o maior foi {} e o menor foi {}' .format(maior, menor))
    print(list)