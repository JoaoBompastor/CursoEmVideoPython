#converter graus celcius para farenheit

grausc = float(input('temperatura em celcius: '))
farenheit = grausc * 1.8 + 32

print('a temperatura original de {} graus celcius, quando convertido para farenheit, fica em {:.1f}f' .format(grausc, farenheit))