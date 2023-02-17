#EU TO FICANDO LOUCO EU ODEIO PA

numero = int(input('digite o primeiro termo de uma pa: '))
razao = int(input('agora, digite a razao dessa pa: '))
count = 0
termos = 0

while count < 10:
    termogeral = numero + count * razao
    print('{} -> ' .format(termogeral), end= '')    

    count += 1

print('FIM')    

count = 0
escolha = int(input('digite quantos termos a mais quer ver: '))

while escolha != 0:
    while count < escolha:
        novotermo = numero + (10 + count) * razao
        print('{} -> ' .format(novotermo), end= '')

        count += 1
    
    escolha = int(input('digite quantos termos a mais quer ver: '))

    termos += 1