# somar impares multiplos de 3 entre 1 e 500

soma = 0
contagem = 0

for c in range (1, 500):
    if c % 2 == 1:
        if c % 3 == 0:
            contagem += 1
            soma += c
            
print('{} fatores, e a soma totaliza {}' .format(contagem, soma))