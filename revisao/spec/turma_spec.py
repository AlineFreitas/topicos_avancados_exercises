# coding: utf-8
import unittest
from should_dsl import should
from ludibrio import Stub
from turma import Turma


class TurmaSpec(unittest.TestCase):

    def test_cadastrar_turma(self):
        with Stub() as um_curso:
            um_curso.nome >> 'Análise de Sistemas'
        self.uma_turma = Turma('Integral', um_curso)
        self.uma_turma.turno |should| equal_to('Integral')
        self.uma_turma.curso.nome |should| equal_to('Análise de Sistemas')
