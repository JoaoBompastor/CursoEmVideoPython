# modulos

def aumentar(numero: float, porcentagem: int):
    return numero + (numero * (porcentagem / 100))


def diminuir(numero: float, porcentagem: int):
    return numero - (numero * (porcentagem / 100))


def dobro(numero: float):
    return numero * 2


def metade(numero: float):
    return numero / 2


def moeda(valor: any):
    return f'R$ {valor :.2f}'
