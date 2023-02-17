#insistir no sexo kkkkkkkkkkkk

sexo = str(input('digite seu sexo: ')).strip() .upper()[0]

while sexo != 'F' and sexo != 'M':
    print('digite um sexo valido: ')

    sexo = str(input('digite seu sexo: ')).strip() .upper()[0]

print('sexo {} registrado com sucesso!' .format(sexo))