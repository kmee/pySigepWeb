# -*- coding: utf-8 -*-
from tag_base import TagBase


class TagServicoAdicional(TagBase):

    TIPO_AVISO_RECEBIMENTO = 'Aviso Recebimento'
    TIPO_MAO_PROPRIA = u'Mão Própria'
    TIPO_VALOR_DECLARADO = 'Valor declarado'
    TIPO_REGISTRO = 'Registor'

    _tipo_servico = {
        TIPO_AVISO_RECEBIMENTO: '001',
        TIPO_MAO_PROPRIA: '002',
        TIPO_VALOR_DECLARADO: '019',
        TIPO_REGISTRO: '025',
    }

    # valor_declarado e obrigatorio apenas para TIPO_VALOR_DECLARADO
    def __init__(self):
        # O Servico Adicional com codigo 025 sempre devera ser informado
        self.lista_tipo_servico_adicional = ['025']
        self.valor_declarado = 0.00

    def add_tipo_servico_adicional(self, tipo_servico_adicional,
                                   valor_declarado=False):

        if tipo_servico_adicional not in TagServicoAdicional._tipo_servico:
            raise KeyError
            return

        if not valor_declarado and self._tipo_servico[
                tipo_servico_adicional] == '019':

            print u'[ALERTA] Para Serviço Adicional do tipo Valor ' \
                  u'Declarado, é obrigatório informar o valor declarado!'
            return

        self.lista_tipo_servico_adicional.append(
            self._tipo_servico[tipo_servico_adicional])
        self.valor_declarado = valor_declarado

    def remove_tipo_servico_adicional(self, tipo_servico_adicional):
        self.lista_tipo_servico_adicional.remove(tipo_servico_adicional)

    def get_tipo_servico_adicional(self, index):
        return self.lista_tipo_servico_adicional[index]

    def get_xml(self):
        xml = u'<servico_adicional>'
        for tipo in self.lista_tipo_servico_adicional:
            xml += u'<codigo_servico_adicional>%s</codigo_servico_adicional>' \
                   % tipo

        xml += u'<valor_declarado>%9.2f</valor_declarado>' % \
               self.valor_declarado

        xml += u'</servico_adicional>'

        self._validar_xml(xml)
        return xml
