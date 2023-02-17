#menu de opcoes SEM funcoes

print('QUADRO DE OPERACOES:')
print('-=-' * 10)

primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))
soma = primeiro_numero + segundo_numero
multiplicacao = primeiro_numero * segundo_numero

print('''OPCOES: 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] comparador
[ 4 ] novos números
[ 5 ] sair do programa
''')

opcao = str(input('Digite uma opcao: ')).strip()

while True:
    if opcao == '1':
        print('A soma entre {} e {} é {}' .format(primeiro_numero, segundo_numero, soma))

    elif opcao == '2':
        print('A multiplicacao entre {} e {} é {}' .format(primeiro_numero, segundo_numero, multiplicacao))
    
    elif opcao == '3':
        if primeiro_numero > segundo_numero:
            print('o numero {} é maior que o numero {}.' .format(primeiro_numero, segundo_numero))
        
        elif primeiro_numero < segundo_numero:
            print('o numero {} é maior que o numero {}.' .format(segundo_numero, primeiro_numero))
        
        else:
            print('Os dois números são iguais!')

    elif opcao == '4':
        primeiro_numero = int(input('Digite o primeiro numero: '))
        segundo_numero = int(input('Digite o segundo numero: '))
    
    elif opcao == '5':
        break
    
    if opcao not in '12345':
        print('opcao invalida.')
    
    print('-=-' * 10)
    print('''OPCOES: 
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] comparador
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')

    opcao = str(input('Digite uma opcao: '))


print('break')