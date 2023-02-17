count = 0

while True:
    print('-' * 20)
    numero = int(input('Digite um numero e saiba a sua tabuada [0 flag]: '))

    if numero <= 0:
        break

    for c in range (1,11):
        print(f'{numero} x {c} = {numero * c}')

    count += 1

print('FIM')