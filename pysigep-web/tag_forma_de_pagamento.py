# -*- coding: utf-8 -*-
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
        xml = u'<forma_pagamento>%s</forma_pagamento>' % aux
        self._validar_xml(xml)
        return xml
