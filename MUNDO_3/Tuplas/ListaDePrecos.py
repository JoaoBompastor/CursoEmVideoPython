count = 0

tupla = (
         'Leite', 6, 
         'frango', 12,
         'pao', 9
         )

print('-=' * 20)
print('NOTA FISCAL' .center(40, ' '))
print('-=' * 20)

for posicao in range(0, len(tupla)):
    if posicao % 2 == 0:
        print(f'{tupla[posicao]:.<30}', end='')

    else:
        print(f'R$ {tupla[posicao]:>7.2f}')

print('-=' * 20)