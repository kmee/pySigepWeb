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


class TagPLP(TagBase):

    def __init__(self, cartao_postagem, valor_global=0.00,
                 mcu_unidade_postagem='', nome_unidade_postagem=''):
        self.id_lpl = False
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
