#calcular o preco final de um produto considerando as condicoes de pagamento

PRECO = float(input('digite o preco do produto e saiba as condicoes de pagamento: '))
DINHEIRO = PRECO - (PRECO * 0.1)
CARTAO = PRECO - (PRECO * 0.05)
CARTAO3X = PRECO + (PRECO * 0.2)

print('-=-' * 20)
print('PRECO A PAGAR: {:.2f}' .format(PRECO))
print('''
    (D) A VISTA:
    (C) CARTAO:
''')

METODO = str(input('Digite sua forma de pagamento: ')).upper().strip()

if METODO == 'D':
    print('-=-' * 20)
    print('pagamento a vista: ')
    print('-=-' * 20)
    print(f'''
        (1) A vista: Dinheiro/Cheque => {DINHEIRO} -10%
        (2) A vista: Cartao => {CARTAO} -5%
    ''')
    print('-=-' * 20)
    DINHEIROOUCARTAO = int(input('Escolha a forma de pagamento: '))

    if DINHEIROOUCARTAO == 1:
        print('o valor final do produto foi de  {:.2f} para {:.2f} de acordo com as condicoes de pagamento!' .format(PRECO, DINHEIRO))
    
    elif DINHEIROOUCARTAO == 2:
        print('O valor final do produto foi de {:.2f} para {:.2f} de acordo com as condicoes de pagamento!' .format(PRECO, CARTAO))
    
    else:
        print('OPCAO INVALIDA, TENTE NOVAMENTE')


elif METODO == 'C':
    print('-=-' * 20)
    print('Pagamento parcelado: ')
    print('-=-' * 20)
    print(f'''
        (3) Ate 2x Cartao => {PRECO} preco normal
        (4) Mais de 3x Cartao => {CARTAO3X} 20% juros
    ''')
    print('-=-' * 20)
    PARCELAS = int(input('Escolha em quantas parcelas pagar, de acordo com a tabela: '))

    if PARCELAS == 3:
        print('O valor final do produto nao sofre alteracao de acordo com as condicoes de pagamento!')
    
    elif PARCELAS == 4:
        print('O valor final do produto foi de {:.2f} para {:.2f} de acordo com as condicoes de pagamento!' .format(PRECO, CARTAO3X))

    else:
        print('OPCAO INVALIDA, TENTE NOVAMENTE')

else:
    print('OPCAO INVALIDA, TENTE NOVAMENTE.')