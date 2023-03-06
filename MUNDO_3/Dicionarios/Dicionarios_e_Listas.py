data:list = []
media_idades:float = 0


while True:
    nome:str = str(input('Nome: ')).strip() .capitalize()
    idade:int = int(input('Idade: '))
    sexo:str = str(input('Sexo: [F/M] ')).strip() .upper()[0]
    media_idades += idade

    Pessoa:dict = {
        'Nome': nome,
        'Idade': idade,
        'Sexo': sexo
    } 
    data.append(Pessoa)

    continuar = str(input('Deseja continuar? [S/N] ')).strip() .upper()[0]

    while continuar not in 'SN': 
        continuar = str(input('Deseja continuar? [S/N] ')).strip() .upper()[0]

    if continuar == 'N':
        break

print(f'O grupo tem {len(data)} pessoas.')
print(f'A média de idade do grupo é {media_idades / len(data)}')
print(f'Mulheres: ', end=' ')

for m in data:
    if Pessoa['Sexo'] in 'Ff':
        print(Pessoa['Nome'], end='')