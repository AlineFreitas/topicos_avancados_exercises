# coding: utf-8
import unittest
from should_dsl import should
from ludibrio import Stub
from curso import Curso


class CursoSpec(unittest.TestCase):

    def test_cadastrar_curso(self):
        self.um_curso = Curso('Análise e Desenvolvimento de Sistemas', 1)
        self.um_curso.nome |should| equal_to('Análise e Desenvolvimento de Sistemas')
        self.um_curso.tipo |should| equal_to('Tecnólogo')
