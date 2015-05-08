# -*- coding: utf-8 -*-


class ResposaFechaPLPVariosServicos(object):

    def __init__(self, xml, id_plp_cliente):
        self._xml = xml
        self.id_plp_cliente = id_plp_cliente

    def salvar_xml(self, path):

        from xml.etree.ElementTree import ElementTree, fromstring

        # tag raiz do xml
        root = fromstring(self.xml.encode('utf8'))

        try:
             # Cria backup do xml retornado
            ElementTree(root).write(path + 'plp_' + str(self.id_plp_cliente) +
                                    '.xml')
        except IOError as excp:
            print '[ERROR] ', excp.message

    @property
    def xml(self):
        return self._xml

