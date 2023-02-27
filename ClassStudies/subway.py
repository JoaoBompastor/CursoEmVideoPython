class sanduiche:
    def __init__(self, pao:str, queijo:str, molho:str) -> str:
        self.pao = pao
        self.queijo = queijo
        self.molho = molho

sub15 = sanduiche('italiano', 'suico', 'chipotle')

print(sub15.molho)