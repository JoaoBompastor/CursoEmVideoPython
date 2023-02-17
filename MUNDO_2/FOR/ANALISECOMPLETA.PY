Lnome = []
Lidade = []
homens = []

mulher = 0
somaidades = 0
maioridade = 0

for c in range(4):
    print('--- {}a PESSOA ---' .format(c + 1))

    nome = str(input('NOME: ')).strip() .capitalize()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [F/M]: ')).strip() .upper()

    somaidades += idade

    if sexo == 'F':
        if idade < 20:
            mulher += 1
    
    elif sexo == 'M':
        homens.append(nome)
        homens.append(idade)

        if c == 0:
            maioridade = idade
                
        elif idade > maioridade:
            maioridade = idade

    Lnome.append(nome)    
    Lidade.append(idade)

print('-=-' * 6)

mediaidades = somaidades / 4
maioridadehomem = homens.index(maioridade)

print('A MEDIA DE IDADE DO GRUPO É: {}' .format(mediaidades))
print('O homem mais velho tem {} anos e se chama {}' .format(maioridade, homens[maioridadehomem - 1]))
print('Ao todo, são {} mulheres abaixo de 20 anos' .format(mulher))