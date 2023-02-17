#criar um programa que le uma frase e identifica se ela eh ou nao um palindromo

frase = str(input('digite uma frase: ')).strip() .upper() .replace(' ', '')

if frase == frase[::-1]:
    print('palindromo')

else:
    print('nao eh palindromo')
