# -*- coding: utf-8 -*-
from tag_base import TagBase


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
        super(TipoObjeto, self).__init__('001')


class Caixa(TipoObjeto):

    def __init__(self, altura, largura, comprimento):
        super(TipoObjeto, self).__init__('002')
        self._altura = altura
        self._largura = largura
        self._comprimento = comprimento


class Cilindro(TipoObjeto):

    def __init__(self, comprimento, diametro):
        super(TipoObjeto, self).__init__('003')
        self._comprimento = comprimento
        self._diametro = diametro


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

        xml = '<dimensao_objeto>'
        xml += '<tipo_objeto>%d</tipo_objeto>' % self.tipo_objeto.codigo
        xml += '<dimensao_altura>%d</dimensao_altura>' % self.tipo_objeto.altura
        xml += '<dimensao_largura>%d</dimensao_largura>' % \
               self.tipo_objeto.largura
        xml += '<dimensao_comprimento>%d</dimensao_comprimento>' % \
               self.tipo_objeto.comprimento
        xml += '<dimensao_diametro>%d</dimensao_diametro>' % \
               self.tipo_objeto.diametro
        xml += '</dimensao_objeto>'

        return xml