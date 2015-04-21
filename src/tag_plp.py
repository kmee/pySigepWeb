# -*- coding: utf-8 -*-
from tag_base import TagBase


class TagPLP(TagBase):

    def __init__(self, cartao_postagem, id_lpl=False, valor_global=0.00,
                 mcu_unidade_postagem='', nome_unidade_postagem=''):
        self.id_lpl = id_lpl
        self.valor_global = valor_global
        self.mcu_unidade_postagem = mcu_unidade_postagem
        self.nome_unidade_postagem = nome_unidade_postagem
        self.cartao_postagem = cartao_postagem

    def get_xml(self):
        xml = u'<plp>'

        aux = str(self.id_lpl) if self.id_lpl else ''
        xml += u'<id_plp>%s</id_plp>' % aux

        aux = str(self.valor_global) if self.valor_global else ''
        xml += u'<valor_global>%s</valor_global>' % aux

        xml += u'<mcu_unidade_postagem>%s</mcu_unidade_postagem>' % \
               self.mcu_unidade_postagem
        xml += u'<nome_unidade_postagem>%s</nome_unidade_postagem>' %  \
               self.nome_unidade_postagem
        xml += u'<cartao_postagem>%s</cartao_postagem>' % self.cartao_postagem
        xml += u'</plp>'

        self._validar_xml(xml)
        return xml
