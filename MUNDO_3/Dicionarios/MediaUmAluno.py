Aluno:dict = {}

Aluno['Nome'] = str(input('Nome: '))
Aluno['Media'] = float(input('Média de {}: ' .format(Aluno['Nome'])))

if Aluno['Media'] < 6:
    Aluno['Situação'] = 'REPROVADO'

else: 
    Aluno['Situação'] = 'APROVADO'

print(f'O nome é igual a: {Aluno["Nome"]}')
print(f'Média é igual a: {Aluno["Media"]}')
print(f'Situação é igual a: {Aluno["Situação"]}')