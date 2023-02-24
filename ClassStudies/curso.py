class Aluno:
    def __init__(self, Nome:str, Idade:int, Nota:float):
        self.Nome = Nome
        self.Idade = Idade
        self.Nota = Nota #  0 - 10

    # retorna a nota do Aluno
    def Get_Nota(self):
        return self.Nota

class Curso:
    def __init__(self, Nome, Max_Alunos):
        self.Nome = Nome
        self.Max_Alunos = Max_Alunos
        self.Alunos:list = []
        self.NotaMinima = 6
    
    # adiciona alunos com a condição do curso não estar lotado
    def Adicionar_Aluno(self, aluno):
        if len(self.Alunos) < self.Max_Alunos:
            self.Alunos.append(aluno)
            return True
            
        else: return False
    
    # remove o ultimo aluno cadastrado
    def Remover_Aluno(self, aluno):
        self.Alunos.pop()

# cadastrando alunos
a1 = Aluno('joao', 17, 6)
a2 = Aluno('matheus', 18, 5)
a3 = Aluno('Luiza', 19, 10)

#criando curso
UPE = Curso('Ciencia da computação', Max_Alunos= 2)

# adicionando alunos
UPE.Adicionar_Aluno(a1)
UPE.Adicionar_Aluno(a2)
UPE.Adicionar_Aluno(a3)

#mostra o nome dos alunos
for c in range(len(UPE.Alunos)):
    print(UPE.Alunos[c].Nome)