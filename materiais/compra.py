class Compra:

    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.produto.incrementar_estoque(quantidade)

