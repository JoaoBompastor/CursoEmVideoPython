class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = (nota1 + nota2) / 2

class App:
    def __init__(self):
        self.Alunos = []

    def adicionar_alunos(self, aluno):
        self.Alunos.append(aluno)

aluno1 = Aluno('joao', 10, 4)
aluno2 = Aluno('luiza', 10, 10)

boletim = App()
boletim.adicionar_alunos(aluno1)
boletim.adicionar_alunos(aluno2)

