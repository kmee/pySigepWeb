# -*- coding: utf-8 -*-
from src import plp_xml_validator
from src.tag_base import TagBase


class TipoObjeto(object):

    _CODIGO = '000'

    def __init__(self, codigo):
        self._CODIGO = codigo
        self.altura = 0
        self.largura = 0
        self.comprimento = 0
        self.diametro = 0

    @property
    def codigo(self):
        return self._CODIGO


class Envelope(TipoObjeto):

    def __init__(self):
        super(Envelope, self).__init__('001')


class Caixa(TipoObjeto):

    def __init__(self, altura, largura, comprimento):
        super(Caixa, self).__init__('002')
        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento


class Cilindro(TipoObjeto):

    def __init__(self, comprimento, diametro):
        super(Cilindro, self).__init__('003')
        self.comprimento = comprimento
        self.diametro = diametro


class TagDimensaoObjeto(TagBase):

    def __init__(self, tipo_objeto):
        self.tipo_objeto = tipo_objeto

        if not isinstance(self.tipo_objeto, TipoObjeto):
            raise TypeError(str(tipo_objeto) + u' não é instancia de '
                                               u'TipoObjeto')

    @property
    def codigo(self):
        return self.tipo_objeto.codigo

    @property
    def altura(self):
        return self.tipo_objeto.altura

    @property
    def largura(self):
        return self.tipo_objeto.largura

    @property
    def comprimento(self):
        return self.tipo_objeto.comprimento

    @property
    def diametro(self):
        return self.tipo_objeto.diametro

    def get_xml(self):

        xml = u'<dimensao_objeto>'
        xml += u'<tipo_objeto>%s</tipo_objeto>' % self.tipo_objeto.codigo
        xml += u'<dimensao_altura>%d</dimensao_altura>' % \
               self.tipo_objeto.altura
        xml += u'<dimensao_largura>%d</dimensao_largura>' % \
               self.tipo_objeto.largura
        xml += u'<dimensao_comprimento>%d</dimensao_comprimento>' % \
               self.tipo_objeto.comprimento
        xml += u'<dimensao_diametro>%d</dimensao_diametro>' % \
               self.tipo_objeto.diametro
        xml += u'</dimensao_objeto>'

        TagDimensaoObjeto.validar_xml(xml)
        return xml

    @staticmethod
    def validar_xml(xml):

        if plp_xml_validator.validate_xml(xml):
            print u'XML TagDimensaoObjeto validado com sucesso!'
        else:
            print u'Validação de XML TagDimensaoObjeto falhou!'