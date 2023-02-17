#programa sorteia 4 alunos, o esculhido eh printado
from random import choice

aluno1 = str(input('aluno 1: '))
aluno2 = str(input('aluno 2: '))
aluno3 = str(input('aluno 3: '))
aluno4 = str(input('aluno 4: '))
alunos = aluno1, aluno2, aluno3, aluno4

escolha = choice(alunos)

print('o aluno sorteado foi {}!' .format(escolha))