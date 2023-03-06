# Cadastro_trabalhador usando poo

class Trabalhador:
    def __init__(self, nome:str, data_nascimento:int, carteira:bool) -> dict:
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.carteira = carteira

Trabalhador1 = Trabalhador('Joao', 2000, True)