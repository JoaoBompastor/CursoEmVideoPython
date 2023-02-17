#contar a quantidade de A em uma string

string = str(input('digite uma frase: '))
String = string.upper()

print('nessa frase, a letra A aparece {} vezes.' .format(String.count('A')))
print('a letra A aparece pela primeira vez na posicao {}' .format(String.find('A')))
print('e aparece por ultimo na posicao {}' .format(String.rfind('A')))