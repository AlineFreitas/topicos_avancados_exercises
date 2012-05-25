import unittest
from should_dsl import should
from ludibrio import Stub
from compra import Compra


class CompraSpec(unittest.TestCase):

    def test_cadastrar_compra(self):
        with Stub() as um_produto:
            #um_produto.estoque >> 10
            um_produto.codigo >> 111
            um_produto.incrementar_estoque(100) >> 110
            um_produto.estoque >> 110
        uma_compra = Compra(um_produto, 100)
        #solucao nao ideal abaixo - problema do __or__()
        uma_compra.produto.codigo |should| equal_to(um_produto.codigo)
        uma_compra.produto.estoque |should| equal_to(110)

