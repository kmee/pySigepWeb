# -*- coding: utf-8 -*-
from endereco import Endereco
from tag_base import TagBase


class TagDestinatario(TagBase):

    def __init__(self, nome, endereco):

        if not isinstance(endereco, Endereco):
            raise TypeError

        self.nome = nome
        self.endereco = endereco
        self.telefone = ''
        self.celular = ''
        self.email = ''
        self.logradouro = ''
        self.complemento = ''
        self.numero_end_destinatario = ''

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

        xml = u'<destinatario>'
        xml += u'<nome_destinatario><![CDATA[%s]]></nome_destinatario>' % \
               self.nome
        xml += u'<telefone_destinatario><![CDATA[' \
               u'%s]]></telefone_destinatario>' % \
               self.telefone
        xml += u'<celular_destinatario><![CDATA[%s]]></celular_destinatario>' \
               % self.celular
        xml += u'<email_destinatario><![CDATA[%s]]></email_destinatario>' % \
               self.email
        xml += u'<logradouro_destinatario><![CDATA[' \
               u'%s]]></logradouro_destinatario>' % self.logradouro
        xml += u'<complemento_destinatario><![CDATA[' \
               u'%s]]><complemento_destinatario>' % self.complemento
        xml += u'<numero_end_destinatario>%s</numero_end_destinatario>' % \
               self.numero
        xml += u'</destinatario>'

        return xml



