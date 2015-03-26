# -*- coding: utf-8 -*-
from base_xml import BaseXML


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


class ServicoAdicional(BaseXML):

    def __init__(self, tipo_servico_adicional):
        if not isinstance(tipo_servico_adicional, TipoServicoAdicional):
            raise TypeError
        self.lista_tipo_servico_adicional = []
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
            xml += '<codigo_servico_adicional>%s</codigo_servico_adicional>' \
                   % sv.codigo
        xml += '<valor_declarado>%s</valor_declarado>' % self.valor_declarado
        return xml

