# -*- coding: utf-8 -*-
from base_xml import BaseXML


class IdPLP(BaseXML):
    def xml(self):
        return '<id_plp>%d</id_plp>' % self._valor


class ValorGlobal(BaseXML):
    def xml(self):
        return '<valor_global>%d</valor_global>' % self._valor


class McuUnidadePostagem(BaseXML):
    def xml(self):
        return '<mcu_unidade_postagem>%d</mcu_unidade_postagem>' % self._valor


class NomeUnidadePostagem(BaseXML):
    def xml(self):
        return '<nome_unidade_postagem>%s</nome_unidade_postagem>' % self._valor


class CartaoPostagem(BaseXML):
    def xml(self):
        return '<cartao_postagem>%d</cartao_postagem>' % self._valor


class PLP(object):

    def __init__(self):
        self.id_lpl = IdPLP()
        self.valor_global = ValorGlobal()
        self.mcu_unidade_postagem = McuUnidadePostagem()
        self.nome_unidade_postagem = NomeUnidadePostagem()
        self.cartao_postagem = CartaoPostagem()

    def xml(self):
        xml = '<plp>'
        xml += self.id_lpl.xml()
        xml += self.valor_global.xml()
        xml += self.mcu_unidade_postagem.xml()
        xml += self.nome_unidade_postagem.xml()
        xml += self.cartao_postagem.xml()
        xml += '</plp>'
        return xml
