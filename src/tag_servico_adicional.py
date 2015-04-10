# -*- coding: utf-8 -*-
from src.tag_base import TagBase


class TipoServicoAdicional(object):

    # def __init__(self):
    #     if not isinstance(valor_declarado, float):
    #         raise TypeError
    #     self.valor_declarado = valor_declarado

    valor_declarado = 0.00

    @property
    def codigo(self):
        pass


class TipoServicoAdicionalAvisoRecebimento(TipoServicoAdicional):
    # def __init__(self):
    #     super(TipoServicoAdicionalAvisoRecebimento, self).__init__()

    @property
    def codigo(self):
        return '001'


class TipoServicoAdicionalMaoPropria(TipoServicoAdicional):
    # def __init__(self):
    #     super(TipoServicoAdicionalMaoPropria, self).__init__()

    @property
    def codigo(self):
        return '002'


class TipoServicoAdicionalValorDeclarado(TipoServicoAdicional):
    def __init__(self, valor_declarado):
        # super(TipoServicoAdicionalValorDeclarado, self).__init__(
        #     valor_declarado)
        TipoServicoAdicionalValorDeclarado.valor_declarado = valor_declarado

    @property
    def codigo(self):
        return '019'


class TipoServicoAdicionalRegistro(TipoServicoAdicional):
    # def __init__(self, valor_declarado=0.00):
    #     super(TipoServicoAdicionalRegistro, self).__init__(
    #         valor_declarado)

    @property
    def codigo(self):
        return '025'


class TagServicoAdicional(TagBase):

    # TIPO_AVISO_RECEBIMENTO = '001'
    # TIPO_MAO_PROPRIA = '002'
    # TIPO_VALOR_DECLARADO = '019'
    # TIPO_REGISTRO = '025'

    # valor_declarado e obrigatorio apenas para TIPO_VALOR_DECLARADO
    def __init__(self):
        self.lista_tipo_servico_adicional = [TipoServicoAdicionalRegistro()]
        # O Servico Adicional com codigo 025 sempre devera ser informado
        # self.lista_tipo_servico_adicional.append(TipoServicoAdicionalRegistro())
        # self.valor_declarado = valor_declarado
        # self.valor_declarado = tipo_servico_adicional.valor_declarado

    def add_tipo_servico_adicional(self, tipo_servico_adicional):
        self.lista_tipo_servico_adicional.append(tipo_servico_adicional)

    def remove_tipo_servico_adicional(self, tipo_servico_adicional):
        self.lista_tipo_servico_adicional.remove(tipo_servico_adicional)

    def get_tipo_servico_adicional(self, index):
        return self.lista_tipo_servico_adicional[index]

    # @property
    # def codigo(self):
    #     return self.tipo_servico_adicional.codigo
    #
    @property
    def valor_declarado(self):
        return self.lista_tipo_servico_adicional[0].valor_declarado

    def get_xml(self):
        xml = u'<servico_adicional>'
        for tipo in self.lista_tipo_servico_adicional:
            xml += u'<codigo_servico_adicional>%s</codigo_servico_adicional>' \
                   % tipo.codigo

        aux = str(self.valor_declarado) if self.valor_declarado else ''
        xml += u'<valor_declarado>%s</valor_declarado>' % aux

        xml += u'</servico_adicional>'

        self._validar_xml(xml)
        return xml
