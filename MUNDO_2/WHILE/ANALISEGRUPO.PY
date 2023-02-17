mulher = homem = maioridade = mulhermenorde20 = 0
homens = []

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)

    idade = int(input('Idade: '))

    if idade >= 13:
        print('Idade inválida para a operação do programa.')
        break

    sexo = str(input('Sexo [F/M]: ')).strip() .upper()[0]

    if idade >= 18:
        maioridade += 1

    if sexo == 'F':
        mulher += 1

        if idade < 20:
            mulhermenorde20 += 1

    if sexo == 'M':
        homem += 1
        homens.append(idade)

    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).strip() .upper()[0]

        if sexo == 'F':
            mulher += 1

            if idade < 20:
                mulhermenorde20 += 1
                
            break

        if sexo == 'M':
            homem += 1
            homens.append(idade)
            break

    print('-' * 20)

    continuar = str(input('Deseja continuar? [S/N] ')).strip() .upper()[0]

    if continuar == 'N':
        break

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip() .upper()[0]

print(' FIM ' .center(21, '='))

print(f'Dentre os dados coletados, existem {maioridade} pessoas maiores de idade')
print(f'Ao todo, existem {len(homens)} homens cadastrados')
print(f'Dentre as mulheres, {mulhermenorde20} sao menores de 20 anos')

print('=' * 20)