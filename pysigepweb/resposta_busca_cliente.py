# -*- coding: utf-8 -*-
from diretoria import *
from servico_postagem import *


class CartaoPostagem(object):

    def __init__(self, status, codigo_admin, numero):
        self.status = status
        self.numero = numero
        self.codigo_admin = codigo_admin
        self.servicos_postagem = []

    def add_servico_postagem(self, codigo, nome, servico_id):
        # self.servicos_postagem.append(ServicoPostagem(int(codigo)))
        self.servicos_postagem.append(ServicoPostagem(int(codigo),
                                                      nome,
                                                      servico_id))


class Contrato(object):

    def __init__(self, codigo_diretoria, id_contrato):
        self.id_contrato = id_contrato
        self.diretoria = Diretoria(int(codigo_diretoria))
        self.cartoes_postagem = []


class RespostaBuscaCliente(object):

    def __init__(self, nome, cnpj, descricao_status_cliente):
        self.nome = nome
        self.cnpj = cnpj
        self.descricao_status_cliente = descricao_status_cliente
        self.contratos = []

