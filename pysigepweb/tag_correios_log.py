# -*- coding: utf-8 -*-
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

        xml = u'<?xml version=\"1.0\" encoding=\"ISO-8859-1\" ?>'
        xml += u'<correioslog>'
        xml += u'<tipo_arquivo>%s</tipo_arquivo>' % TagCorreiosLog._TIPO_ARQUIVO
        xml += u'<versao_arquivo>%s</versao_arquivo>' % self.versao
        xml += self.tagPLP.get_xml()
        xml += self.tag_remetente.get_xml()
        xml += self.forma_pagamento.get_xml()
        for objeto_postal in self.lista_objeto_postal:
            xml += objeto_postal.get_xml()
        xml += u'</correioslog>'

        if self._validar_xml(xml):
            return xml

        return None
