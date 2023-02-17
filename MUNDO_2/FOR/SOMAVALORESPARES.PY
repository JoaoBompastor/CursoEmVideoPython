#ler seis numeros inteiros e printar a soma dos valores pares

soma = 0
valores_aceitos = []
valores_descartados = []

for numeros in range (0, 6):
    valores = int(input('digite um numero: '))

    if valores % 2 == 0:
        soma += valores
        valores_aceitos.append(valores)
    
    else:
        valores_descartados.append(valores)

print('-=-' * 20)

print('A soma dos valores pares dessa lista foi: {}' .format(soma))
print('os valores aceitos foram: {}' .format(valores_aceitos))
print('e os valores descartados foram: {}' .format(valores_descartados))

print('-=-' * 20)