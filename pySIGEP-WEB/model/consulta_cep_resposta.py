# -*- coding: utf-8 -*-


class ConsultaCEPResposta(object):

    def __init__(self, bairro, cep, end, cep_id, uf, complemento=None,
                 complemento2=None):
        self.bairro = bairro
        self.cep = cep
        self.complemento = complemento
        self.complemento2 = complemento2
        self.end = end
        self.cep_id = cep_id
        self.uf = uf
