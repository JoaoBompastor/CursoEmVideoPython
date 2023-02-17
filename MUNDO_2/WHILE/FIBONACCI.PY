numero = int(input('digite quantos digitos de fibonacci vc quer ver: '))
termo1 = 0
termo2 = 1
count = 3

print('{} -> {} -> ' .format(termo1, termo2), end='')

while count <= numero:    
    termo3 = termo1 + termo2

    print('{} -> ' .format(termo3), end='')

    termo1 = termo2
    termo2 = termo3

    count += 1

print('FIM')