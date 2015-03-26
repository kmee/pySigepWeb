# -*- coding: utf-8 -*-
from tag_base import TagBase


class TagPLP(TagBase):

    def __init__(self, cartao_postagem):
        self.id_lpl = 0
        self.valor_global = 0.00
        self.mcu_unidade_postagem = ''
        self.nome_unidade_postagem = ''
        self.cartao_postagem = cartao_postagem

    def xml(self):
        xml = '<plp>'
        xml += '<id_plp>%s</id_plp>' % str(self.id_lpl) or ''
        xml += '<valor_global>%s</valor_global>' % str(self.valor_global) or ''
        xml += '<mcu_unidade_postagem>%s</mcu_unidade_postagem>' % \
               self.mcu_unidade_postagem
        xml += '<nome_unidade_postagem>%s</nome_unidade_postagem>' %  \
               self.nome_unidade_postagem
        xml += '<cartao_postagem>%s</cartao_postagem>' % self.cartao_postagem
        xml += '</plp>'
        return xml
