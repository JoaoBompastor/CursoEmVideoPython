def double(lista:list) -> list:
    novalista:list = []

    for numero in lista:
        novalista.append(numero * 2)
    
    print(novalista)


ls1:list = [1, 2, 3, 4]
ls2:list = [2, 3, 4, 5]

double(ls1)
double(ls2)