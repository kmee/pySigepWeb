# -*- coding: utf-8 -*-
from base_xml import BaseXML


class Nacional(BaseXML):

    def __init__(self, endereco, numero_nfe, serie_nfe, valor_a_cobrar):
        self.endereco = endereco
        self.codigo_usuario_postal = ''
        self.centro_custo_cliente = ''
        self.num_nfe = numero_nfe
        self.serie_nfe = serie_nfe
        self.valor_nfe = 0.00
        self.natureza_nfe = ''
        self.descricao_objeto = ''
        self.valor_a_cobrar = valor_a_cobrar

    def get_xml(self):

        xml = '<nacional>'
        xml += '<bairro_destinatario>%s</bairro_destinatario>' % \
               self.endereco.bairro
        xml += '<cidade_destinatario>%s</cidade_destinatario>' % \
               self.endereco.cidade
        xml += '<uf_destinatario>%s</uf_destinatario>' % self.endereco.uf
        xml += '<cep_destinatario>%s</cep_destinatario>' % self.endereco.cep
        xml += '<codigo_usuario_postal>%s</codigo_usuario_postal>' % \
               self.codigo_usuario_postal
        xml += '<centro_custo_cliente>%s</centro_custo_cliente>' % \
               self.centro_custo_cliente
        xml += '<numero_nota_fiscal>%d</numero_nota_fiscal>' % self.num_nfe
        xml += '<serie_nota_fiscal>%s</serie_nota_fiscal>' % self.serie_nfe
        xml += '<valor_nota_fiscal>%s</valor_nota_fiscal>' % str(self.valor_nfe)
        xml += '<natureza_nota_fiscal></natureza_nota_fiscal>'
        xml += '<descricao_objeto>%s</descricao_objeto>' % self.descricao_objeto
        xml += '<valor a cobrar>%s</valor a cobrar>' % str(self.valor_a_cobrar)
        xml += '</nacional>'

        return xml