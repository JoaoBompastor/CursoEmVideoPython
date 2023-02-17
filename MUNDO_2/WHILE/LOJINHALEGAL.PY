continuar = total = maisbarato = acimademil =  0
nomebarato = ''

print('-' * 40)
print('LOJA MANEIRA' .center(40, ' '))
print('-' * 40)

while True:
    nome = str(input('Nome do produto: ')).strip() .upper()
    preco = int(input('Preco: R$'))

    if preco > 1000:
        acimademil += 1
    
    if maisbarato == 0:
        maisbarato = preco
        nomebarato = nome
    
    if preco < maisbarato:
        maisbarato = preco
        nomebarato = nome

    total += preco

    continuar = str(input('Deseja continuar? [S/N] ')).strip() .upper()[0]
    
    if continuar == 'N':
        break

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip() .upper()[0]
    
    print('-' * 40)

print(' FIM DO PROGRAMA ' .center(40, '-'))
print(f'\nA o valor final do carrinho foi R${total}')
print(f'No carrinho, existem {acimademil} itens acima de 1000 reais')
print(f'O produto mais barato dentro do carrinho é {nomebarato.capitalize()} e custou R${maisbarato}')
