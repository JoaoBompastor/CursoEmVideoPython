def get_fatorial(numero: int = 1, show: bool = False):
    '''
    -> funcao que mostra o fatorial de um numero qualquer
    :param numero: numero inteiro qualquer, default = 1
    :param show: valor booleano que define se o programa mostra o processo da conta,
                 default = False
    '''
    print('=' * 20)

    fatorial = 1
    for c in range(numero, 0, -1):
        fatorial *= c

        if show == True:
            if c != 1:
                print(c, end=' x ')

            else:
                print(c, end=' = ')

    return fatorial


# Main
print(get_fatorial(7, show= True))
print(help(get_fatorial))