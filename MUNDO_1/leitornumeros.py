#ler um numero de 0 a 9999 e mostrar os digitos separados

numero = str(input('digite um numero de 0 - 9999: ')).strip()
separar = ' '.join(numero)
separado = separar.rsplit(' ')
