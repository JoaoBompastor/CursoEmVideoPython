numeros = (
    'zero', 
    'um', 
    'dois', 
    'tres', 
    'quatro', 
    'cinco', 
    'seis', 
    'sete', 
    'oito', 
    'nove', 
    'dez', 
    'onze', 
    'doze', 
    'treze',
    'quatorze', 
    'quinze', 
    'dezesseis', 
    'dezesete', 
    'dezoito',
    'dezenove', 
    'vinte'
)

while True:
    print('=' * 40)

    numero = int(input('Digite um numero entre 0 e 20: '))

    while numero < 0 or numero > 20:
        numero = int(input('Escolha inválida, Digite um numero entre 0 e 20: '))

    print(f'Voce digitou o número {numeros[numero]}!')

    continuar = str(input('Deseja continuar? ')).strip() .upper()[0]

    if continuar == 'N':
        break

print('FIM')