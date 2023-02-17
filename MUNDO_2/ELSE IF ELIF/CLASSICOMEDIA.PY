#DESAFIO classico da media com aprovacao/reprovacao. media 7

Primeira_nota = float(input('digite a primeira nota: '))
Segunda_nota = float(input('digite a segunda nota: '))
media = (Primeira_nota + Segunda_nota) / 2

if media >= 7:
    print('APROVADO! média {:.1f}' .format(media))

elif 7 > media >= 5:
    print('RECUPERACAO! média obtida: {:.1f}' .format(media))

else:
    print('REPROVADO. média mínima necessária: 5\nmédia obtida: {:.1f}' .format(media))