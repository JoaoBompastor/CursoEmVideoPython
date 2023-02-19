people:list = []
data:list = []
CountMaior = CountMenor = 0

#coleta dados de pessoas e armazena na lista 'people'
while True:
    data.append(str(input('Digite seu nome: ')).strip() .capitalize())
    data.append(int(input('Digite sua idade: ')))
    people.append(data[:])
    data.clear()

    print('-=' * 20)

    continuar = str(input('Deseja continuar? [s/n] ')).strip() .upper()[0]

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [s/n] ')).strip() .upper()[0]
    
    if continuar == 'N':
        break


#checa maioridade loopando cada item dentro de people, o indice indica uma pessoa dentro da lista.
for pessoa in people:
    if pessoa[1] >= 18:
        CountMaior += 1
    
    else:
        CountMenor += 1

print(f'O total de pessoas adicionadas foi: {len(people)}')
print(f'E os nomes das pessoas adicionadas sao: {[pessoa[0] for pessoa in people]}')
print(f'As pessoas cadastradas foram: {people}')
print(f'O total de pessoas maiores de idade foi: {CountMaior}')
print(f'O total de pessoas menores de idade foi: {CountMenor}')