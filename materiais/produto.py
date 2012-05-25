class Produto:
    produtos = []

    @classmethod
    def listar_produtos(cls):
        return cls.produtos

    def __init__(self, codigo, descricao):
        self.codigo = codigo
        self.descricao = descricao
        self.estoque = 0
        Produto.produtos.append(self)

    def incrementar_estoque(self, quantidade):
        self.estoque += quantidade

    def decrementar_estoque(self, quantidade):
        self.estoque -= quantidade

