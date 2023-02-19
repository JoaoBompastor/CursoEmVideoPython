lista = []

while True:
    numero = int(input('Digite um numero: '))

    lista.append(numero)

    continuar = str(input('Deseja continuar? [s/n] ')).strip() .upper()[0]

    if continuar == 'N':
        break

print(f'Voce digitou {len(lista)} valores.')
print(f'Os valores digitados, em ordem decrescente sao: {sorted(lista, reverse=True)}')

if 5 in lista:
    print(f'O valor 5 foi encontrado na posicao {lista.index(5) + 1} da lista.')

else:
    print('O valor 5 nao foi encontrado na lista')
