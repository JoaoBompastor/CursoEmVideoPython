#programa le a velocidade de um carro e o multa se ultrapassar 80kmh, 7 reais por km excedente

velocidade = float(input('qual eh a velocidade atual do carro? '))

if velocidade <= 80:
    print('td certinho patrao! tenha um bom dia.')
else:
    multa = (velocidade - 80) * 7
    print('''
        voce ultrapassou o limite de 80km/h!
        voce sera multado em R${:.2f}!
        dirija com seguranca!
    ''' .format(multa))