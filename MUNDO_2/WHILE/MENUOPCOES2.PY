#menu de opcoes COM funcoes

maior = 0

print('PAINEL DE FUNCOES: ')
print('-=-' * 10)

primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))

print('-=-' * 10)
print('''ACOES:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] comparar
[ 4 ] novos números
[ 5 ] sair do programa''')
print('-=-' * 10)

escolha = str(input('Que acao deseja realizar? '))

def adicao():
    return primeiro_numero + segundo_numero

def multiplicacao():
    return primeiro_numero * segundo_numero

def comparar():
    if primeiro_numero > segundo_numero:
        maior = primeiro_numero
    
    elif primeiro_numero < segundo_numero:
        maior = segundo_numero
    
    else:
        print('Os dois números são iguais!')
    
    return maior

while True:
    if escolha == '1':
        print('O resultado da adição entre {} e {} é {}' .format(primeiro_numero, segundo_numero, adicao()))

    if escolha == '2':
        print('O resultado entre {} e {} é {}' .format(primeiro_numero, segundo_numero, multiplicacao()))

    if escolha == '3':
        print('Entre o número {} e {}, o número {} é maior.' .format(primeiro_numero, segundo_numero, comparar()))

    if escolha == '4':
        primeiro_numero = int(input('Digite o primeiro numero: '))
        segundo_numero = int(input('Digite o segundo numero: '))

    if escolha == '5':
        print('FECHAR O PROGRAMA: ')
        certeza = str(input('Voce tem certeza? ')).strip() .upper()
        
        if certeza == 'S':
            break

        if certeza == 'N':
            primeiro_numero = int(input('Digite o primeiro numero: '))
            segundo_numero = int(input('Digite o segundo numero: '))
    
    if escolha not in '12345':
        print('OPCAO INVALIDA.')

        primeiro_numero = int(input('Digite o primeiro numero: '))
        segundo_numero = int(input('Digite o segundo numero: '))

    print('-=-' * 10)
    print('''ACOES:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] comparar
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    print('-=-' * 10)

    escolha = str(input('Que acao deseja realizar? '))

print('Break')