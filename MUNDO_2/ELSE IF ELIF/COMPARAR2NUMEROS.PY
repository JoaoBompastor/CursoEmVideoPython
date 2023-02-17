#comparar dois numeros, dizer se sao maiores que ou iguais uns aos outros

Primeiro_numero = float(input('digite o primeiro numero: '))
Segundo_numero = float(input('digite o segundo numero: '))

if(Primeiro_numero > Segundo_numero):
    print('o PRIMEIRO valor eh maior')

elif(Segundo_numero > Primeiro_numero):
    print('o SEGUNDO valor eh maior')

else:
    print('OS VALORES SAO IGUAIS')