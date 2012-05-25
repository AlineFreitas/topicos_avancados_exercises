class Venda:

    def __init__(self, produto, quantidade):
        self.eh_valida = (quantidade <= produto.estoque)
        self.produto = produto
        self.quantidade = quantidade
        if self.eh_valida:
           self.produto.decrementar_estoque(quantidade)

