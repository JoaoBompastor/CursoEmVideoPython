#ler um numero inteiro e dizer se ele eh primo ou nao (e contar divisibilidades)
import colors

numero = int(input('digite um numero e saiba se ele eh primo: '))
divisivel = []

for c in range (1, numero + 1):
    if numero % c == 0:
        print(colors.green, end='')
        divisivel.append(c)
    
    else:
        print(colors.red, end='')
    
    print('{} ' .format(c), end='')

print('\n{}o numero {} foi divisivel {} vezes.' .format(colors.none, numero, len(divisivel)))

if len(divisivel) > 2:
    print('e por isso ele NAO EH PRIMO')

else:
    print('e por isso ele EH PRIMO')