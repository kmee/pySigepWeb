# -*- coding: utf-8 -*-


class Usuario(object):

    def __init__(self, nome, senha, cnpj, num_contrato, num_cartao_postagem):
        self.nome = nome
        self.senha = senha
        self.num_contrato = num_contrato
        self.num_cartao_postagem = num_cartao_postagem
        self.cnpj = cnpj
