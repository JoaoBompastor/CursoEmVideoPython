lista:list = []
pares:list = []
impares:list = []

for c in range (7):
    lista.append(int(input('Digite um numero: ')))

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

    else:
        impares.append(numero)

print(lista)
print(sorted(pares))
print(sorted(impares))