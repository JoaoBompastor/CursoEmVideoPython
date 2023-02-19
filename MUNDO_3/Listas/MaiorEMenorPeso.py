people:list = []
data:list = []
pesos:list = []

#MainLoop
while True:
    data.append(str(input('Digite seu nome: ')).strip() .capitalize())
    data.append(float(input('Digite seu peso (kg): ')))
    people.append(data[:])
    data.clear()

    continuar = str(input('Deseja continuar? [s/n] ')).strip() .upper()[0]

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [s/n] ')).strip() .upper()[0]

    if continuar == 'N':
        break

for pessoas in people:
    pesos.append(pessoas[1])

print(f'Ao todo, voce pesou {len(people)} pessoas.')
print(people)
print(f'O maior peso registrado foi {max(pesos)}. Pessoas com esse peso: ', end='')

for pessoa in people:
    if pessoa[1] == max(pesos):
        print(pessoa[0], end=' ')

print(f'\nO menor peso registrado foi de: {min(pesos)}. Pessoas com esse peso: ', end='')

for pessoa in people:
    if pessoa[1] == min(pesos):
        print(pessoa[0], end=' ')