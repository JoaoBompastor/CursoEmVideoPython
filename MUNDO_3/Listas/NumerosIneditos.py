lista = []

while True:
    numero = int(input('Logue um numero no sistema: '))

    if numero in lista:
        print('Numero ja cadastrado, nao vou registrar...')

    else:
        lista.append(numero)

    print('-=' * 20)

    continuar = str(input('Deseja continuar? [S/N] ')).strip() .upper()[0]

    if continuar == 'N':
        break

    print('-=' * 20)

print('=' * 40)

print('Valores registrados: ', end='')

for c in sorted(lista):
    print(c, end=' ')