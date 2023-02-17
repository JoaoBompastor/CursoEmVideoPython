#comparar 3 numeros

n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
n3 = float(input('digite o terceiro numero: '))

if n1 < n2 and n1 < n3:
    print('o menor numero eh {}' .format(n1))
if n2 < n1 and n2 < n3:
    print('o menor numero eh {}' .format(n2))
if n3 < n1 and n3 < n2:
    print('o menor numero eh {}' .format(n3))

if n1 > n2 and n1 > n3:
    print('o maior numero eh {}' .format(n1))
if n2 > n1 and n2 > n3:
    print('o maior numero eh {} ' .format(n2))
if n3 > n2 and n3 > n1:
    print('o maior numero eh {}' .format(n3))
