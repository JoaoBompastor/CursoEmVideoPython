#programa checa o ano de nascimento de alguem, diz quantos anos tem hj em dia e fala sobre o alistamento, se e quando (ano) deve fazer

nascimento = int(input('digite o ano do seu nascimento: '))
ano = 2017
idade = ano - nascimento

if(idade < 18):
    falta = (18 - idade) + ano

    print('''
    voce ainda nao possui 18 anos!
    em {}, vc tem {} anos, poderá se alistar em {}!
    ''' .format(idade, falta))

elif(idade > 18):
    alistou = str(input('voce ja se alistou?\ns/n: '))
    
    if(alistou == 's'):
        print('muito bem comparsinha!')
    
    else:
        passou = idade - 18

        print('''
        voce tem {} anos
        voce TEM que se alistar!
        era para voce ter se alistado a {} anos!
        ''' .format(idade, passou))

else:
    print('PARABENS! voce completa(ou) 18 anos esse ano! esta na hora de se alistar!')
