# coding: utf-8
class Curso(object):
    tipos = {1: 'Tecnólogo', 2: 'Bacharelado'}
    
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = self.tipos[tipo]
