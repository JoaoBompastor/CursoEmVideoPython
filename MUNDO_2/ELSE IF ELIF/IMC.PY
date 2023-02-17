#calcular IMC e retornar resultado

PESO = int(input('digite o seu peso: (kg) '))
ALTURA = float(input('digite sua altura: (m) '))
IMC = PESO / (ALTURA**2)

if IMC < 18.5:
    print('ABAIXO DO PESO {:.1f}' .format(IMC))

elif IMC <= 25:
    print('PESO IDEAL {:.1f}' .format(IMC))

elif IMC <= 30:
    print('SOBREPESO {:.1f}' .format(IMC))

elif IMC <= 40:
    print('OBESIDADE {:.1f}' .format(IMC))

else:
    print('OBESIDADE MORBIDA {:.1f}' .format(IMC))
