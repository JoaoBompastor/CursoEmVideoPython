
km = float(input('quantos km o carro rodou? '))
dias = int(input('quantos dias o carro foi alugado? '))

print('sabendo q o carro rodou por {}km e foi alugado num total de {} dias, o preco total da conta sera de {}' .format(km, dias, (km * 0.15) + (60 * dias)))