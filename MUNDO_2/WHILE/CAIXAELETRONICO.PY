print('=' * 20)
print('BANCO JSB' .center(20, ' '))
print('=' * 20)

saque = int(input('Quanto deseja sacar? R$'))
total = saque
cedula = 50
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1

    else:
        if total_cedulas > 0:
            print(f'{total_cedulas} cedulas de {cedula}')

        if cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 1

        total_cedulas = 0
        
        if total == 0:
            break