from time import sleep

def counter(inicio:int, fim:int, passo:int) -> int:
    if passo == 0:
        passo = 1

    if inicio > fim:
        passo *= -1
        fim -= 1

    else:
        fim += 1

    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.3)

    print('\n')

counter(1, 10, 1)
print('-=' * 10)
counter(10, 0, 2)

print('Agora é a sua vez! selecione um início e um fim pra contagem: ')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

counter(inicio, fim, passo)