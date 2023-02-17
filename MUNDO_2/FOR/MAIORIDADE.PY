#checar a maioridade de 7 pessoas por intermedio de seu ano de nascimento

from datetime import datetime

ano_atual = datetime.now().year
maior = 0
menor = 0

for c in range (1, 8):
    ano = int(input('em que ano nasceu a {}a pessoa? ' .format(c)))

    if ano_atual - ano >= 18:
        maior += 1
    
    else:
        menor += 1

print('Ao todo, tivemos {} pessoas maior de idade' .format(maior))
print('E tivemos {} pessoas menor de idade.' .format(menor))
