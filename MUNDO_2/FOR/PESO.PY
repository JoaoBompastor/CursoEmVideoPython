#ler 5 pesos em kg :.1f e printar o maior/menor entre eles

list = []

for c in range (1, 6):
    peso = float(input('peso da {}a pessoa: ' .format(c)))

    list.append(peso)
    
print('o maior peso foi {} e o menor peso foi {}' .format(max(list), min(list)))