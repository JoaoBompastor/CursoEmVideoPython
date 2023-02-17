#reajuste: > 1250 == 10% \\ <= 1250 == 15%

salario = float(input('digite seu slario e saiba o valor do seu reajuste: '))

if salario <= 1250.0:
    ajuste =  salario + (salario * 0.15)
else:
    ajuste = salario + (salario * 0.10)

print('o seu salario pos reajuste sera de R${}' .format(ajuste))