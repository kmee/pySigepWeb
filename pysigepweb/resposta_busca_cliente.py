# -*- coding: utf-8 -*-
# #############################################################################
#
#    Brazillian Carrier Correios Sigep WEB
#    Copyright (C) 2015 KMEE (http://www.kmee.com.br)
#    @author: Michell Stuttgart <michell.stuttgart@kmee.com.br>
#
#    Sponsored by Europestar www.europestar.com.br
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from diretoria import *
from servico_postagem import *


class CartaoPostagem(object):
    def __init__(self, status, codigo_admin, numero):
        self.status = status
        self.numero = numero
        self.codigo_admin = codigo_admin

        # chave:codigo do servico
        self.servicos_postagem = {}

    def add_servico_postagem(self, codigo, nome, servico_id):
        self.servicos_postagem[codigo] = ServicoPostagem(int(codigo),
                                                         nome,
                                                         servico_id)


class Contrato(object):
    def __init__(self, codigo_diretoria, id_contrato):
        self.id_contrato = id_contrato
        self.diretoria = Diretoria(int(codigo_diretoria))

        # chave:numero do cartao de postagem
        self.cartoes_postagem = {}


class Cliente(object):

    def __init__(self, nome, login, senha, cnpj, descricao_status_cliente=''):
        self.nome = nome
        self.login = login
        self.status = descricao_status_cliente
        self.senha = senha

        cnpj = cnpj.replace('.', '')
        cnpj = cnpj.replace('/', '')
        cnpj = cnpj.replace('-', '')
        self.cnpj = cnpj

        # chave:id do contrato
        self.contratos = {}

    def get_contrato(self, id_contrato):
        return self.contratos[id_contrato]

    def get_cartao_postagem(self, id_contrato, numero_cartao):
        return self.contratos[id_contrato].cartoes_postagem[numero_cartao]

    def get_servico_postagem(self, id_contrato, numero_cartao,
                             codigo_servico):
        return self.contratos[id_contrato].cartoes_postagem[
            numero_cartao].servicos_postagem[codigo_servico]

    def get_lista_cartao_postagem(self, id_contrato):
        return self.contratos[id_contrato].cartoes_postagem

    def get_lista_servico_postagem(self, id_contrato, numero_cartao):
        return self.contratos[id_contrato].cartoes_postagem[
            numero_cartao].servicos_postagem



