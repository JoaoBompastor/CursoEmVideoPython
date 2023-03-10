from datetime import datetime


def voto(ano_nascimento:int) -> str:
    idade = datetime.today().year - ano_nascimento

    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: Voto obrigatorio.'

    elif idade >= 16 and idade < 18 or idade >= 65:
        return f'Com {idade} anos: Voto facultativo.'

    else:
        return f'Com {idade} anos: Voto negado.'


# Main
ano_nascimento = int(input('Em que ano voce nasceu? '))
print(voto(ano_nascimento))