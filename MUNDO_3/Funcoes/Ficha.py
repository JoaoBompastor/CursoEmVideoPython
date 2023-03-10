def Ficha(nome_do_jogador: str, quantidade_gols: str):
    print('-' * 20)

    if nome_do_jogador == '':
        nome_do_jogador = '<desconhecido>'

    if quantidade_gols == '':
        quantidade_gols = '0'

    print(f'O jogador {nome_do_jogador} fez {quantidade_gols} gol(s) no campeonato.')


# Main
nome_do_jogador = str(input('Nome: ')).strip()
quantidade_gols = str(input('Quantidade de gols: '))
Ficha(nome_do_jogador= nome_do_jogador, quantidade_gols= quantidade_gols)