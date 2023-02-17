Maioridade = CountHomem = mulhermenorde20 =  0

while True:
    print('-=-' * 10)

    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'FfMm':
        sexo = str(input('Sexo: ')).strip() .upper()[0]

        if sexo == 'M':
            CountHomem += 1

        elif sexo == 'F' and idade < 20:
            mulhermenorde20 += 1

    if idade >= 18:
        Maioridade += 1

    print('-=-' * 10)

    continuar = str(input('Deseja continuar cadastrando? ')).strip() .upper()[0]

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar cadastrando? ')).strip() .upper() [0]

    if continuar == 'N':
        break

print(f'{Maioridade} maiores de 18')
print(f'{CountHomem} homens cadastrados')
print(f'{mulhermenorde20} mulheres menores de 20 anos')