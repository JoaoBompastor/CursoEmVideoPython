lista = []

for c in range (5):
    numero = int(input('Digite um numero: '))

    if c == 0:
        lista.append(numero)
        print('Adicionado ao inicio da lista.')

    elif numero < min(lista):
        lista.insert(0, numero)
        print('Adicionado ao inicio da lista.')

    else:
        if numero > max(lista):
            lista.append(numero)
            print('Adicionado ao final da lista.')

print(f'Os valores digitados, em ordem: {lista}')

# outra solucao:
# for c in range (5):
#     numero = int(input('Digite um numero: '))

#     if c > numero:
#         lista.insert(0, numero)

#     else:
#         lista.append(numero)