nome = str(input('digite seu nome completo: ')).strip()
split = nome.split()
Pnome = split[0]
Unome = split[-1]

print('''
    {}
    {}
    {}
''' .format(nome.title(), Pnome.capitalize(), Unome.capitalize()))
