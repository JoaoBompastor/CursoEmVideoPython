count = numero = soma = 0

while True:
    numero = int(input('Digite um numero: [101 to Break] '))
    
    if numero == 101:
        break

    print(numero, soma, count)

    count += 1
    soma += numero

print('Voce digitou {} números, e a soma entre eles foi {}' .format(count, soma))
