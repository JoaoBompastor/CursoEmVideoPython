#ler o primeiro termo de uma PA e sua razao, e mostrar os primeiros 10 termos

termo = int(input('digite o termo da P.A: '))
razao = int(input('digite a razao da P.A: '))
decimo = termo + (10 - 1) * razao

for c in range (termo, decimo + razao, razao):
    print(c)

print('ACABOU!')
