#checar a possibilidade de formar um triangulo

a = float(input('digite um dos lados do seu triangulo: '))
b = float(input('digite o segundo lado do seu triangulo: '))
c = float(input('digite o terceiro lado do seu triangulo: '))

if a < b + c and c < b + a and b < c + a:
    print('esse triangulo pode ser formado')
else:
    print('esse triangulo nao pode ser formado')