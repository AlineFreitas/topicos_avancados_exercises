import unittest
from should_dsl import should
from produto import Produto


class ProdutoSpec(unittest.TestCase):

    def setUp(self):
        self.um_produto = Produto(10,'Toalha')

    def test_cadastrar_produto(self):
        #um_produto = Produto(10,'Toalha')
        self.um_produto.codigo |should| equal_to(10)
        self.um_produto.descricao |should| equal_to('Toalha')
        self.um_produto.estoque |should| equal_to(0)

    def test_incrementar_estoque(self):
        #self.um_produto = Produto(10,'Toalha')
        self.um_produto.incrementar_estoque(10)
        self.um_produto.incrementar_estoque(50)
        self.um_produto.estoque |should| equal_to(60)

    def test_decrementar_estoque(self):
        #self.um_produto = Produto(10,'Toalha')
        self.um_produto.incrementar_estoque(10)
        self.um_produto.decrementar_estoque(5)
        self.um_produto.estoque |should| equal_to(5)

    def test_listar_produtos(self):
        produto1 = Produto(1,'A')
        produto2 = Produto(2,'A')
        produto3 = Produto(3,'A')
        Produto.listar_produtos() |should| include(produto1)

