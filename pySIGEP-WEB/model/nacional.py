# -*- coding: utf-8 -*-


class DestinoNacional(object):

    def __init__(self, endereco):
        self.bairro = endereco.bairro
        self.cep = endereco.cep
        self.cidade = endereco.cidade
        self.uf = endereco.uf
