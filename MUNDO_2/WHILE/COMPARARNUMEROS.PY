count = soma = media = maior = 0
menor = 1
list = []

#considera o primeiro numero
numero = int(input('Digite um numero: '))
confirmacao = str(input('Quer continuar? [S/N] '))
count += 1
soma += numero
list.append(numero)

#considera todos os numeros depois do primeiro
while confirmacao in 'Ss':
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    numero = int(input('Digite um numero: '))
    confirmacao = str(input('Quer continuar? [S/N] '))
    count += 1
    soma += numero
    list.append(numero)

#considera o ultimo numero
else:
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    print(list)
    media = soma / count
    print('Voce digitou {} numeros, e a média entre eles foi {}' .format(count, media))
    print('O maior valor entre eles foi {}, e o menor foi {}' .format(maior, menor))
