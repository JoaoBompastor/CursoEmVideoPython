#ler um nome
#apresentar o nome em upper
#apresentar o nome em lower
#contar letras sem espaco
#contar letras primeiro nome

nome = str(input('digite um nome: ')) .strip()
primeironome = nome[:nome.find(' ')]

print('o seu nome, inteiramente em letras maiusculas fica: {}' .format(nome.upper()))
print('o seu nome, inteiramente em letras minusculas fica: {}' .format(nome.lower()))
print('o seu nome, sem espaços, contem {} letras!' .format(len(nome.replace(' ' , ''))))
print('e o seu primeiro nome é {}, e contem {} letras!' .format(primeironome, len(primeironome)))