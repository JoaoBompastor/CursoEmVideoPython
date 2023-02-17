expressao = []
letras = []
ParentesesCount = 0

E = str(input('Digite uma expressao: ')).strip()
expressao.append(E)

for item in expressao:
    for letra in item:
        if letra in '()':
            ParentesesCount += 1

if ParentesesCount % 2 == 0:
    print('Essa expressao é valida!')

else:
    print('Essa expressao nao é valida.')
