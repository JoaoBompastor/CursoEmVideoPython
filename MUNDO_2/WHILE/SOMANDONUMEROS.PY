soma = numeros = usuario = 0

while usuario != 999:
    usuario = int(input('digite um numero [999 para parar]: '))

    soma += usuario
    numeros +=1

print('voce digitou {} numeros.' .format(numeros - 1))
print('e a soma deles foi {}' .format(soma - 999))
