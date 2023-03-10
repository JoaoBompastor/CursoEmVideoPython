from Print_bonitinho import escreva
import colors

# Main
while True:
    print(colors.green)
    escreva('SISTEMA DE AJUDA PyHelp!')

    print(colors.none)
    escolha = str(input('Funcao ou biblioteca > ')).strip() .lower()

    while escolha != 'fim':
        print(colors.yellow)
        escreva(f'Acessando o manual do comando {escolha}')
        help(escolha)

        print(colors.none)
        escolha = str(input('Funcao ou biblioteca > ')).strip() .lower()

    break


print(colors.red)
escreva('fim')
print(colors.none)