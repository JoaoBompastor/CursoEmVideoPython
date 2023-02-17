#calculadora!

def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2 

def divisao(n1, n2):
    return n1 / n2

print('1) adição')
print('2) subtração')
print('3) multiplicação')
print('4) divisão')

escolha = input('escolha uma operação: ')

if escolha in ('1', '2', '3', '4'):
    try:
        n1 = int(input('primeiro numero:'))
        n2 = int(input('segundo numero: '))
    except ValueError:
        print('syntax error')

if escolha == '1':
    print('a soma entre {} e {} é {}!' .format(n1, n2, adicao(n1, n2)))

if escolha == '2':
    print('a diferença entre {} e {} é {}!' .format(n1, n2, subtracao(n1, n2)))

if escolha == '3':
    print('a multiplicação entre {} e {} é {}!' .format(n1, n2, multiplicacao(n1, n2)))

if escolha == '4':
    print('a divisão entre {} e {} é {}!' .format(n1, n2, divisao(n1, n2)))