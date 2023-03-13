def LeiaInt(frase: str):
    while True:
        n = input(frase)
        
        if n.isnumeric():
            valor = int(n)
            break
        
        else:
            print('Valor invalido')

    return valor


# Main
n = LeiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')