import unittest
from should_dsl import should
from ludibrio import Stub
from venda import Venda


class VendaSpec(unittest.TestCase):

    def test_cadastrar_venda_valida(self):
        with Stub() as um_produto:
            um_produto.codigo >> 111
            um_produto.estoque >> 10
            um_produto.decrementar_estoque(5) >> 'Qualquer coisa!'
        venda_valida = Venda(um_produto, 5)
        venda_valida.eh_valida |should| equal_to(True)

    def test_venda_invalida(self):
        with Stub() as um_produto:
            um_produto.codigo >> 111
            um_produto.estoque >> 10
        venda_invalida = Venda(um_produto, 15)
        venda_invalida.eh_valida |should| equal_to(False)

