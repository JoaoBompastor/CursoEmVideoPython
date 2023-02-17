#perguntar valor casa, salario e tempo do emprestimo (anos), prestacao mensal n pode exceder 30% salario ou sera negada
print('-=-' * 20)
print('aprovacao de emprestimo pra comprar uma casa')
print('-=-' * 20)

casa = float(input('digite o valor da casa: '))
salario = float(input('digite o seu salario para avaliacao: '))
tempo = int(input('digite em quantos anos pretende quitar a casa: '))
prestacao = casa / (tempo * 12)

print('-=-' * 20)

if(prestacao <= salario * 0.3):
    print('APROVADO! a prestacao ficará no valor de R${:.2f}' .format(prestacao))

else:
    print('NEGADO! a prestacao ficará em R${:.2f}, oq eh inviavel para seu salario de R${:.2f}' .format(prestacao, salario))
