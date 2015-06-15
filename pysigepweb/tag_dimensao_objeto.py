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
from dimensao import *


class TagDimensaoObjeto(Dimensao, TagBase):

    def __init__(self, codigo, altura=2, largura=11, comprimento=16, diametro=5):
        super(TagDimensaoObjeto, self).__init__(codigo, altura, largura,
                                                comprimento, diametro)

    def get_xml(self):

        xml = u'<dimensao_objeto>\n'
        xml += u'<tipo_objeto>%s</tipo_objeto>\n' % self.codigo
        xml += u'<dimensao_altura>%d</dimensao_altura>\n' % self.altura
        xml += u'<dimensao_largura>%d</dimensao_largura>\n' % self.largura
        xml += u'<dimensao_comprimento>%d</dimensao_comprimento>\n' % \
               self.comprimento
        xml += u'<dimensao_diametro>%d</dimensao_diametro>\n' % self.diametro
        xml += u'</dimensao_objeto>\n'

        self._validar_xml(xml)
        return xml
