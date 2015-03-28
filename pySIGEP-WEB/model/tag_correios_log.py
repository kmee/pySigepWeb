# -*- coding: utf-8 -*-
from tag_base import TagBase


class TagCorreiosLog(TagBase):

    _TIPO_ARQUIVO = 'Postagem'

    def __init__(self, versao, obj_tag_plp, obj_tag_remetente,
                 lista_tag_objeto_pastal):
        self.versao = versao
        self.forma_pagamento = ''
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
        xml += u'<forma_pagamento></forma_pagamento>'
        for objeto_postal in self.lista_objeto_postal:
            xml += objeto_postal.get_xml()
        xml += u'</correioslog>'

        TagCorreiosLog.validar_xml(xml)
        return xml

    @staticmethod
    def validar_xml(xml):
        import plp_xml_validator

        if plp_xml_validator.validate_xml(xml):
            print u'XML TagCorreiosLog validado com sucesso!'
        else:
            print u'Validação de XML TagCorreiosLog falhou!'

