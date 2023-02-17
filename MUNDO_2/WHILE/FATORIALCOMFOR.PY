from math import factorial

numero = int(input('digite um numero: '))
print(numero, end= '')
for c in range (numero - 1, 0, -1): print(' x {}' .format(c), end= '')
print(' = {}' .format(factorial(numero)))