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
from tag_base import TagBase


class TagDestinatario(TagBase):

    def __init__(self, nome, endereco, telefone=False, celular=False, email=''):
        self.nome = nome
        self.endereco = endereco
        self.celular = celular
        self.email = email

        if telefone:
            telefone = telefone.replace('-', '')
            telefone = telefone.replace(' ', '')
            telefone = telefone.replace('(', '')
            telefone = telefone.replace(')', '')

        self._telefone = telefone

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

    @property
    def complemento(self):
        return self.endereco.complemento

    @complemento.setter
    def complemento(self, valor):
        self.endereco.complemento = valor

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, value):
        value = value.replace('-', '')
        value = value.replace(' ', '')
        value = value.replace('(', '')
        value = value.replace(')', '')
        self._telefone = value

    def get_xml(self):

        xml = u'<destinatario>'
        xml += u'<nome_destinatario><![CDATA[%s]]></nome_destinatario>' % \
               self.nome

        aux = str(self.telefone) if self.telefone else ''
        xml += u'<telefone_destinatario><![CDATA[' \
               u'%s]]></telefone_destinatario>' % aux

        aux = str(self.celular) if self.celular else ''
        xml += u'<celular_destinatario><![CDATA[%s]]></celular_destinatario>' \
               % aux

        xml += u'<email_destinatario><![CDATA[%s]]></email_destinatario>' % \
               self.email
        xml += u'<logradouro_destinatario><![CDATA[' \
               u'%s]]></logradouro_destinatario>' % self.logradouro
        xml += u'<complemento_destinatario><![CDATA[' \
               u'%s]]></complemento_destinatario>' % self.complemento
        xml += u'<numero_end_destinatario>%s</numero_end_destinatario>' % \
               str(self.numero)
        xml += u'</destinatario>'

        self._validar_xml(xml)
        return xml
