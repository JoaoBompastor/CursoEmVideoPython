from datetime import datetime

Trabalhador:dict = {}

Trabalhador['Nome'] = str(input('Nome: ')).strip() .upper()

ano_de_nascimento = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano_de_nascimento

Trabalhador['Idade'] = idade
Trabalhador['CTPS'] = int(input('Carteira de trabalho: [0 nao tem] '))

if Trabalhador['CTPS'] != 0:
    Trabalhador['Contratação'] = int(input('Ano de contratação: '))

    anos_trabalhados = Trabalhador['Contratação'] - ano_de_nascimento

    Trabalhador['Salário'] = float(input('Salário: '))
    Trabalhador['Aposentadoria'] = (35 - anos_trabalhados) + idade

for key, values in Trabalhador.items():
    print(key, values)