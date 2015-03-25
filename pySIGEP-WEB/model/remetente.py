# -*- coding: utf-8 -*-
from endereco import Endereco
from base_xml import BaseXML


class Remetente(BaseXML):

    def __init__(self, nome, num_contrato, codigo_admin, endereco, diretoria):

        if not isinstance(endereco, Endereco):
            raise TypeError

        self.nome = nome
        self.num_contrato = num_contrato
        self.codigo_admin = codigo_admin
        self.endereco = endereco
        self.diretoria = diretoria
        self.telefone = 999999999999
        self.fax = 999999999999
        self.email = ''

    @property
    def logradouro(self):
        return self.endereco.logradouro

    @logradouro.setter
    def logradouro(self, valor):
        self.endereco.logradouro = valor

    @property
    def numero(self):
        return self.endereco.numero

    @numero.setter
    def numero(self, valor):
        self.endereco.numero = valor

    @property
    def bairro(self):
        return self.endereco.bairro

    @bairro.setter
    def bairro(self, valor):
        self.endereco.bairro = valor

    @property
    def cep(self):
        return self.endereco.cep

    @cep.setter
    def cep(self, valor):
        self.endereco.cep = valor

    @property
    def cidade(self):
        return self.endereco.cidade

    @cidade.setter
    def cidade(self, valor):
        self.endereco.cidade = valor

    @property
    def uf(self):
        return self.endereco.uf

    @uf.setter
    def uf(self, valor):
        self.endereco.uf = valor

    def get_xml(self):

        xml = '<remetente>'
        xml += '<numero_contrato>%s</numero_contrat o>' % self.num_contrato
        xml += self.diretoria.xml()
        xml += '<codigo_administrativo>%s</codigo_administrativo>' % \
               self.codigo_admin
        xml += '<nome_remetente>%s</nome_remetente>' % self.nome
        xml += '<logradouro_remetente>%s</logradouro_remetente>' % \
               self.logradouro
        xml += '<numero_remetente>%d</numero_remetente>' % self.numero
        xml += '<complemento_remetente>%s</complemento_remetente>' % \
               self.endereco.complemento
        xml += '<bairro_remetente>%s</bairro_remetente>' % self.bairro
        xml += '<cep_remetente>%s</cep_remetente>' % self.cep
        xml += '<cidade_remetente>%s</cidade_remetente>' % self.cidade
        xml += '<uf_remetente>%s</uf_remetente>' % self.uf
        xml += '<telefone_remetente>%s</telefone_remetente>' % self.telefone
        xml += '<fax_remetente>%s</fax_remetente>' % self.fax
        xml += '<email_remetente>%s</email_remetente>' % self.email
        xml += '</remetente>'

        return xml

