numeros = []
pares = []
impares = []

while True:
    numero = int(input('Digite um numero: '))

    numeros.append(numero)

    continuar = str(input('Deseja continuar? [s/n] ')).strip() .upper()[0]

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [s/n] ')).strip() .upper()[0]

    if continuar == 'N':
        break
    
for valor in numeros:
    if valor % 2 == 0:
        pares.append(valor)

    else:
        impares.append(valor)

print(f'Todos os valores digitados: {numeros}')
print(f'Somente os valores pares: {pares}')
print(f'Somente os valores impares: {impares}')
