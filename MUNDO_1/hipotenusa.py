#desafio! ler cateto oposto e adjacente e calcular a hipotenusa
from math import hypot

Coposto = float(input('qual eh a medida do cateto oposto? '))
Cadjacente = float(input('e a medida do adjacente? '))

print('em um triangulo com cateto oposto {}, e adjacente {}, sua hipotenusa vale {:.2f}!' .format(Coposto, Cadjacente, hypot(Coposto, Cadjacente)))