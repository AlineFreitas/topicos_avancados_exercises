# coding: utf-8
import unittest
from should_dsl import should
from ludibrio import Stub
from turma import Turma
from curso import Curso
from aluno import Aluno


class IntegrationTurmaSpec(unittest.TestCase):

    def setUp(self):
        self.aluno = Aluno('Aline', '200821200065')
        self.curso = Curso('Sistemas de Informação', 2)
        self.turma = Turma('Integral', self.curso)

    def test_enturmar_aluno(self):
        self.turma.enturmar_aluno(self.aluno)
        self.turma.alunos |should| include(self.aluno)

    def test_listar_alunos(self):
        aluno2 = Aluno('Rebeca', '200821200060')
        aluno3 = Aluno('Jefferson', '200821200062')
        aluno4 = Aluno('Rui', '200821200061')
        aluno5 = Aluno('Tayná', '200821200069')
        
        self.turma.enturmar_aluno(aluno2)
        self.turma.enturmar_aluno(aluno3)
        self.turma.enturmar_aluno(aluno4)
        self.turma.enturmar_aluno(aluno5)
        
        self.turma.alunos |should| include(aluno2) and include(aluno3) and include(aluno4) and include(aluno5)
