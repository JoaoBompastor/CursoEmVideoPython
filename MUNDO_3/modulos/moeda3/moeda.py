# modulos

def moeda(valor: any):
    """
    funcao fundamental que determina a formatacao de um valor monetario
    (reutilizada em outras funcoes)
    """
    return f'R${valor :.2f}'


def aumentar(numero: float, porcentagem: int, formated: bool):
    """
    retorna o valor passado no parametro numero com um acrecimo determinado pelo param porcentagem
    """
    valor_aumentado: float = numero + (numero * (porcentagem / 100))

    if formated:
        return moeda(valor_aumentado)

    else:
        return valor_aumentado


def diminuir(numero: float, porcentagem: int, formated: bool):
    """
    funcao que retorna o valor passado no parametro numero com um decrecimo determinado pelo param porcentagem
    """
    valor_diminuido: float = numero - (numero * (porcentagem / 100))

    if formated:
        return moeda(valor_diminuido)

    else:
        return valor_diminuido


def dobro(numero: float, formated: bool):
    """
    funcao que retorna o dobro do valor passado no parametro numero
    """
    valor_dobrado: float = numero * 2

    if formated:
        return moeda(valor_dobrado)

    else:
        return valor_dobrado


def metade(numero: float, formated: bool):
    """
    funcao que retorna metade do valor passado no parametro numero
    """
    valor_metade: float = numero / 2

    if formated:
        return moeda(valor_metade)

    else:
        return valor_metade


def resumo(valor: float, acrecimo: int, decrecimo: int):
    print('-' * 30)
    print('RESUMO DO VALOR' .center(30))
    print('-' * 30)
    print(f'''    
Preco analisado: {valor}
Dobro do preco: {dobro(valor, formated=True)}
Metade do preco: {metade(valor, formated=True)}
{acrecimo}% de aumento: {aumentar(valor, acrecimo, formated=True)}
{decrecimo}% de reducao: {diminuir(valor, decrecimo, formated=True)}''')
    print('-' * 30)
