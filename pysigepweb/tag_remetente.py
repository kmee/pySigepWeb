# -*- coding: utf-8 -*-
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

        xml = u'<remetente>'

        xml += u'<numero_contrato>%s</numero_contrato>' % self.num_contrato
        xml += self.diretoria.get_xml()
        xml += u'<codigo_administrativo>%s</codigo_administrativo>' % \
               self.codigo_admin
        xml += u'<nome_remetente><![CDATA[%s]]></nome_remetente>' % self.nome
        xml += u'<logradouro_remetente><![CDATA[%s]]></logradouro_remetente>' % \
               self.logradouro
        xml += u'<numero_remetente>%d</numero_remetente>' % self.numero
        xml += u'<complemento_remetente><![CDATA[%s]]></complemento_remetente>' \
               % self.endereco.complemento
        xml += u'<bairro_remetente><![CDATA[%s]]></bairro_remetente>' % \
               self.bairro
        xml += u'<cep_remetente><![CDATA[%s]]></cep_remetente>' % self.cep
        xml += u'<cidade_remetente><![CDATA[%s]]></cidade_remetente>' % \
               self.cidade
        xml += u'<uf_remetente>%s</uf_remetente>' % self.uf

        aux = str(self.telefone) if self.telefone else ''
        xml += u'<telefone_remetente><![CDATA[%s]]></telefone_remetente>' % aux

        aux = str(self.fax) if self.fax else ''
        xml += u'<fax_remetente><![CDATA[%s]]></fax_remetente>' % aux

        xml += u'<email_remetente><![CDATA[%s]]></email_remetente>' % self.email
        xml += u'</remetente>'

        self._validar_xml(xml)
        return xml
