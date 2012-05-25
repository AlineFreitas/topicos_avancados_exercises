#coding: utf-8
class Turma(object):

    def __init__(self, turno, curso):
        self.turno = turno
        self.curso = curso
        self.alunos = []

    def enturmar_aluno(self, aluno):
        self.alunos.append(aluno)
        aluno.set_turma(self)

    def listar_alunos(self):
        for aluno in self.alunos:
            print aluno.nome, aluno.matricula
    
    
if __name__ == "__main__":
    from aluno import Aluno
    from curso import Curso
    
    aluno1 = Aluno('Karollyne','200821200077')
    aluno2 = Aluno('Rebeca', '200821200060')
    aluno3 = Aluno('Jefferson', '200821200062')
    aluno4 = Aluno('Rui', '200821200061')
    aluno5 = Aluno('Tayná', '200821200069')

    curso1 = Curso('Sistemas de Informação', 2)
    curso2 = Curso('Análise e Desenvolvimento de Sistemas', 1)

    turma1 = Turma('Integral', curso1)
    print '%s em %s - %s' %(turma1.curso.tipo, turma1.curso.nome, turma1.turno)
    turma2 = Turma('Noturno', curso2)
    print '%s - %s' %(turma2.curso.nome, turma2.turno)
    
    turma1.enturmar_aluno(aluno1)
    turma1.enturmar_aluno(aluno4)
    turma1.enturmar_aluno(aluno5)

    turma2.enturmar_aluno(aluno2)
    turma2.enturmar_aluno(aluno3)

    print '----------------------------------------------------------'    

    turma1.listar_alunos()

    print '----------------------------------------------------------'
    turma2.listar_alunos()
