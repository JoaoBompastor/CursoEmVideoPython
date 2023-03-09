def Maior(*args:int) -> int:
    print('-=' * 15)
    print('analisando os valores passados...')

    for c in args:
        print(c, end=' ')

    print(f'foram informados {len(args)} valores ao todo.')
    print(f'O maior valor informado foi {max(args)}.')


Maior(1, 2, 3, 4)
Maior(0, 1, 2)
Maior(0)