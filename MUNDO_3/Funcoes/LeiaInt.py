def LeiaInt(frase: str, n: int = 1):
    n = input(frase)

    while n not in '1234567890':
        print('Numero invalido! tente novamente.')
        n = input(frase)


# Main
n = LeiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')