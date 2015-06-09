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


class TagFormaDePagamento(TagBase):

    VALE_POSTAL = 'VALE_POSTAL'
    REEMBOLSO_POSTAL = 'REEMBOLSO_POSTAL'
    CONTRATO_DE_CAMBIO = 'CONTRATO_DE_CAMBIO'
    CARTAO_DE_CREDITO = 'CARTAO_DE_CREDITO'
    OUTROS = 'OUTROS'
    A_FATURAR = 'A_FATURAR'

    _formas_de_pagamento = {
        VALE_POSTAL: ('Vale postal', 1),
        REEMBOLSO_POSTAL: ('Reembolso postal', 2),
        CONTRATO_DE_CAMBIO: ('Contrato de cambio', 3),
        OUTROS: ('Outros', 5),
        A_FATURAR: ('A faturar', False)
    }

    def __init__(self, forma_de_pagamento):
        self._valor = TagFormaDePagamento._formas_de_pagamento.get(
            forma_de_pagamento)

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, forma_de_pagamento):
        self._valor = TagFormaDePagamento._formas_de_pagamento.get(
            forma_de_pagamento)

    def get_xml(self):
        aux = str(self.valor) if self.valor[1] else ''
        xml = u'<forma_pagamento>%s</forma_pagamento>\n' % aux
        self._validar_xml(xml)
        return xml
