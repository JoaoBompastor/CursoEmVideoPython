from random import randint

print('roleta russa :)')
print('*' * 20)

trigger = str(input('apertar o gatilho? '))

if trigger == 's':

    random = randint(1, 8)
    escolha = randint(1, 8)

    if random == escolha:
        print('morreu.')

    else:
        print('se safou dessa comparsinha! a bala estava no compartimento {}, e vc tirou o compartimento {}' .format(random, escolha))

else:
    print('invalid syntax')
    
print('*' * 20)