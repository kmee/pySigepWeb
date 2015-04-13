# -*- coding: utf-8 -*-
from tag_base import TagBase
from dimensao import *


class TagDimensaoObjeto(Dimensao, TagBase):

    def __init__(self, tipo_objeto):
        super(TagDimensaoObjeto, self).__init__(tipo_objeto)

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

        self._validar_xml(xml)
        return xml
