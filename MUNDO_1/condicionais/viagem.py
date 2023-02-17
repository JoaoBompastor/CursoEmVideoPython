distancia = float(input('digite a distancia da sua viagem, em km: '))

if distancia > 200:
    taxa = distancia * 0.45
    print('''
        em sua viagem, voce percorrera {}km
        e sua passagem custara R${:.2f}
    ''' .format(distancia, taxa))
else:
    taxa = distancia * 0.5
    print('''
        em sua viagem, voce percorrera {}km
        e sua passagem custara R${:.2f}
    ''' .format(distancia, taxa))
