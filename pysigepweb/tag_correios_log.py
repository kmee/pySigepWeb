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
from tag_forma_de_pagamento import TagFormaDePagamento


class TagCorreiosLog(TagBase):

    _TIPO_ARQUIVO = 'Postagem'

    def __init__(self, versao, obj_tag_plp, obj_tag_remetente,
                 lista_tag_objeto_pastal,
                 obj_forma_de_pagamento=TagFormaDePagamento.A_FATURAR):
        self.versao = versao
        self.forma_pagamento = TagFormaDePagamento(obj_forma_de_pagamento)
        self.tagPLP = obj_tag_plp
        self.tag_remetente = obj_tag_remetente
        self.lista_objeto_postal = lista_tag_objeto_pastal

    @property
    def tipo_arquivo(self):
        return TagCorreiosLog._TIPO_ARQUIVO

    def get_xml(self):

        xml = u'<?xml version=\"1.0\" encoding=\"ISO-8859-1\" ?>\n'
        xml += u'<correioslog>\n'
        xml += u'<tipo_arquivo>%s</tipo_arquivo>\n' % TagCorreiosLog._TIPO_ARQUIVO
        xml += u'<versao_arquivo>%s</versao_arquivo>\n' % self.versao
        xml += self.tagPLP.get_xml()
        xml += self.tag_remetente.get_xml()
        xml += self.forma_pagamento.get_xml()
        for objeto_postal in self.lista_objeto_postal:
            xml += objeto_postal.get_xml()
        xml += u'</correioslog>\n'

        if self._validar_xml(xml):
            return xml

        return None
