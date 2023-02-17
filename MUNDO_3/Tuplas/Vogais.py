tupla = (
    'aprender',
    'programar',
    'linguagem',
    'python',
    'curso',
    'gratis',
    'estudar',
    'praticar',
    'trabalhar',
    'mercado',
    'programador',
    'futuro'
)

print(tupla)

for palavras in range (0, len(tupla)):
    palavra = tupla[palavras].upper()

    print(f'\nna palavra {palavra} temos as vogais: ', end='')
    
    for letra in range (0, len(palavra)):
        if palavra[letra] in 'AEIOU':
            print(palavra[letra], end=' ')
