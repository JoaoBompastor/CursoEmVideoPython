soma = numero = count = 0

while True:
    numero = int(input('Digite um numero [999 flag]: '))

    if numero == 999:
        break

    count += 1
    soma += numero

print('Voce digitou {} números, e a soma deles foi {}' .format(count, soma))