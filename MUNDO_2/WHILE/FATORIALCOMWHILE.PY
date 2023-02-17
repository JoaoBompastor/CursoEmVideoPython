from math import factorial

numero = int(input('digite um numero e saiba seu fatorial: '))
count = numero - 1

print(numero, end= '')

while count > 0:
    print(' x {}' .format(count), end= '')
    count -= 1

print(' = {}' .format(factorial(numero)))