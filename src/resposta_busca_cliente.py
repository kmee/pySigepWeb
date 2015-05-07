# -*- coding: utf-8 -*-
__author__ = 'michell'
from diretoria import *
from servico_postagem import *


class CartaoPostagem(object):

    def __init__(self, status, codigo_admin):
        self.status = status
        self.codigo_admin = codigo_admin
        self.servicos_postagem = []

    def add_servico_postagem(self, codigo):
        self.servicos_postagem.append(ServicoPostagem(codigo))


class Contrato(object):

    def __init__(self, codigo_diretoria):
        self.diretoria = Diretoria(int(codigo_diretoria))
        self.cartoes_postagem = []


class RespostaBuscaCliente(object):

    def __init__(self, nome, cnpj, descricao_status_cliente):
        self.nome = nome
        self.cnpj = cnpj
        self.descricao_status_cliente = descricao_status_cliente
        self.contratos = []
