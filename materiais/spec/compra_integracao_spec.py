import unittest
from should_dsl import should
from produto import Produto
from compra import Compra


class CompraIntegracaoSpec(unittest.TestCase):

    def test_cadastrar_compra(self):
        um_produto = Produto(111,'Agulha')
        uma_compra = Compra(um_produto, 100)
        #solucao nao ideal abaixo - problema do __or__()
        uma_compra.produto.codigo |should| equal_to(um_produto.codigo)
        uma_compra.produto.estoque |should| equal_to(100)

