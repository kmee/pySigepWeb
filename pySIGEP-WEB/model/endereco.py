# -*- coding: utf-8 -*-


class Endereco(object):

    def __init__(self, logradouro, numero, bairro, cep, cidade, uf):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
