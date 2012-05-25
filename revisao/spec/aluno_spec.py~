import unittest
from should_dsl import should
from ludibrio import Stub
from aluno import Aluno


class AlunoSpec(unittest.TestCase):

    def test_cadastrar_aluno(self):
        self.um_aluno = Aluno('Creusa','200821200056')
        self.um_aluno.nome |should| equal_to('Creusa')
        self.um_aluno.matricula |should| equal_to('200821200056')
