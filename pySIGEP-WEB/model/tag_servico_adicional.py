# -*- coding: utf-8 -*-
from tag_base import TagBase


class TipoServicoAdicional(object):

    _CODIGO = '000'

    def __init__(self, codigo, valor_declarado=0.0):
        self._CODIGO = codigo

        if not isinstance(valor_declarado, float):
            raise TypeError
        self.valor_declarado = valor_declarado

    @property
    def codigo(self):
        return self._CODIGO


class AvisoRecebimento(TipoServicoAdicional):
    def __init__(self, valor_declarado=0.0):
        super(AvisoRecebimento, self).__init__('001', valor_declarado)


class MaoPropria(TipoServicoAdicional):
    def __init__(self, valor_declarado=0.0):
        super(AvisoRecebimento, self).__init__('002', valor_declarado)


class ValorDeclarado(TipoServicoAdicional):
    def __init__(self, valor_declarado):
        super(AvisoRecebimento, self).__init__('019', valor_declarado)


class Registro(TipoServicoAdicional):
    def __init__(self, valor_declarado=0.0):
        super(AvisoRecebimento, self).__init__('025', valor_declarado)


class TagServicoAdicional(TagBase):

    def __init__(self):
        self.lista_tipo_servico_adicional = []
        # O Servico Adicional com codigo 025 sempre devera ser informado
        self.lista_tipo_servico_adicional.append(Registro())

    def add_tipo_servico_adicional(self, tipo_servico_adicional):
        self.lista_tipo_servico_adicional.append(tipo_servico_adicional)

    def remove_tipo_servico_adicional(self, tipo_servico_adicional):
        self.lista_tipo_servico_adicional.remove(tipo_servico_adicional)

    def get_tipo_servico_adicional(self, index):
        return self.lista_tipo_servico_adicional[index]

    @property
    def codigo(self):
        return self.tipo_servico_adicional.codigo

    @property
    def valor_declarado(self):
        return self.tipo_servico_adicional.valor_declarado

    def get_xml(self):
        xml = ''
        for sv in self.lista_tipo_servico_adicional:
            xml += u'<codigo_servico_adicional>%s</codigo_servico_adicional>' \
                   % sv.codigo
        xml += u'<valor_declarado>%s</valor_declarado>' % str(
            self.valor_declarado) if self.valor_declarado else ''
        return xml

