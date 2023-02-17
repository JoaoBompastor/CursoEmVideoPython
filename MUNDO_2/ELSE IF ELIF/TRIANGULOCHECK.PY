#checar se triangulo eh possivel, dps dizer o tipo do triangulo

LADO_1 = int(input('comprimento do primeiro segmento: '))
LADO_2 = int(input('comprimento do segundo segmento: '))
LADO_3 = int(input('comprimento do terceiro segmento: '))

if LADO_1 < LADO_2 + LADO_3 and LADO_2 < LADO_1 + LADO_3 and LADO_3 < LADO_1 + LADO_2:
    print('esse triangulo eh possivel.')

    if LADO_1 == LADO_2 == LADO_3:
        print('e esse triangulo eh EQUILATERO!')
    
    elif LADO_1 != LADO_2 != LADO_3 != LADO_1:
        print('triangulo ESCALENO')

    else:
        print('triangulo ISOCELES')

else:
    print('esse triangulo eh impossivel.')