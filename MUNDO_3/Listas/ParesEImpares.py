lista:list = []
pares:list = []
impares:list = []

for numeros in range (7):
    lista.append(int(input('Digite um numero: ')))

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

    else:
        impares.append(numero)

print(f'Os valores pares digitados, em forma crescente foi: {sorted(pares)}')
print(f'Os valores impares digitados, em forma crescente foi: {sorted(impares)}')