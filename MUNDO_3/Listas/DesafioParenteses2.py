# fazer o DesafioParenteses em um loop

expressao = []
letras = []
ParentesesCount = 0

while True:

    print('=' * 40)
    print('VALIDADOR DE EXPRESSOES!' .center(40, ' '))
    print('=' * 40)

    E = str(input('Digite uma expressao matematica com parenteses: ')).strip()
    expressao.append(E)

    for item in expressao:
        for letra in item:
            if letra in '()':
                ParentesesCount += 1

    if ParentesesCount % 2 == 0:
        print('Essa expressao é valida!')

    else:
        print('Essa expressao é invalida.')

    print('=' * 40)
    
    continuar = str(input('Deseja continuar? [S/N] ')).strip() .upper()[0]

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip() .upper()[0]

    if continuar == 'N':
        break

print('FIM')