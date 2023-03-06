DataBase:list = []

while True:
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    nota = float(input('Digite sua nota: '))

    Pessoa:dict = {
        'Nome': nome,
        'Idade': idade,
        'Nota': nota
    }
    DataBase.append(Pessoa)

    continuar = str(input('Deseja continuar cadastrando pessoas? [S/N] ')).strip() .upper()[0]

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar cadastrando pessoas? [S/N] ')).strip() .upper()[0]

    if continuar == 'N':
        break

print('Alunos registrados')

for count, item in enumerate(DataBase):
    print(count, item['Nome'])

analisar_aluno:int = int(input('Deseja ver a nota de que aluno? [999 flag] '))
