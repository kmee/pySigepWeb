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


class TagRemetente(TagBase):
    def __init__(self, nome, num_contrato, codigo_admin, endereco, diretoria,
                 telefone=False, fax=False, email=''):

        self.nome = nome
        self.num_contrato = num_contrato
        self.codigo_admin = codigo_admin
        self.endereco = endereco
        self.diretoria = diretoria
        self.telefone = telefone
        self.fax = fax
        self.email = email

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

        xml = u'<remetente>\n'

        xml += u'<numero_contrato>%s</numero_contrato>\n' % self.num_contrato
        xml += self.diretoria.get_xml()
        xml += u'<codigo_administrativo>%s</codigo_administrativo>\n' % \
               self.codigo_admin
        xml += u'<nome_remetente><![CDATA[%s]]></nome_remetente>\n' % self.nome
        xml += u'<logradouro_remetente><![CDATA[%s]]></logradouro_remetente>\n' % \
               self.logradouro
        xml += u'<numero_remetente>%d</numero_remetente>\n' % self.numero
        xml += u'<complemento_remetente><![CDATA[%s]]></complemento_remetente>\n' \
               % self.endereco.complemento
        xml += u'<bairro_remetente><![CDATA[%s]]></bairro_remetente>\n' % \
               self.bairro
        xml += u'<cep_remetente><![CDATA[%s]]></cep_remetente>\n' % self.cep
        xml += u'<cidade_remetente><![CDATA[%s]]></cidade_remetente>\n' % \
               self.cidade
        xml += u'<uf_remetente>%s</uf_remetente>\n' % self.uf

        aux = str(self.telefone) if self.telefone else ''
        xml += u'<telefone_remetente><![CDATA[%s]]></telefone_remetente>\n' % aux

        aux = str(self.fax) if self.fax else ''
        xml += u'<fax_remetente><![CDATA[%s]]></fax_remetente>\n' % aux

        xml += u'<email_remetente><![CDATA[%s]]></email_remetente>\n' % self.email
        xml += u'</remetente>\n'

        self._validar_xml(xml)
        return xml
