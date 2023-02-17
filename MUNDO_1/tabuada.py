#tabuada! (to orgulhoso disso)
numero = int(input('digite um numero e saiba sua tabuada: '))
tabuada = 1 

print('-' * 20)
for i in range(10):
    print('{} x {} = {}' .format(numero, tabuada , numero * tabuada))
    tabuada += 1
print('-' * 20)