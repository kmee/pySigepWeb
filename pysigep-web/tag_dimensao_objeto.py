# -*- coding: utf-8 -*-
from tag_base import TagBase
from dimensao import *


class TagDimensaoObjeto(Dimensao, TagBase):

    def __init__(self, tipo_objeto):
        super(TagDimensaoObjeto, self).__init__(tipo_objeto)

    def get_xml(self):

        xml = u'<dimensao_objeto>'
        xml += u'<tipo_objeto>%s</tipo_objeto>' % self.tipo_objeto.codigo
        xml += u'<dimensao_altura>%d</dimensao_altura>' % self.altura
        xml += u'<dimensao_largura>%d</dimensao_largura>' % self.largura
        xml += u'<dimensao_comprimento>%d</dimensao_comprimento>' % \
               self.comprimento
        xml += u'<dimensao_diametro>%d</dimensao_diametro>' % self.diametro
        xml += u'</dimensao_objeto>'

        self._validar_xml(xml)
        return xml
