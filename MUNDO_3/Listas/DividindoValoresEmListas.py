lista = []
pares = []
impares = []

while True:
    numero = int(input('Digite um numero: '))

    lista.append(numero)

    if numero % 2 == 0:
        pares.append(numero)

    else:
        impares.append(numero)

    print('-=' * 20)

    continuar = str(input('Deseja continuar? ')).strip() .upper()[0]

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? ')).strip() .upper()[0]

    if continuar == 'N':
        break

print(f'Todos os numeros: {lista}')
print(f'Somente pares: {pares}')
print(f'Somente impares: {impares}')