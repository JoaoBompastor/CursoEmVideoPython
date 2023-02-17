#wow hahahaha como eu amo progressao aritimetica!

numero = int(input('digite um numero e saiba da sua progressao aritimetica: '))
razao = int(input('Agora, digite a razao da progressao: '))
count = 0

while count < 10:
    termo = numero + count * razao

    print('{} -> ' .format(termo), end= '')

    count += 1

print('Fim!') 