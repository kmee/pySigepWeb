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


class TagNacional(TagBase):

    def __init__(self, endereco):
        self.endereco = endereco
        self.codigo_usuario_postal = ''
        self.centro_custo_cliente = ''
        self.num_nfe = False
        self.serie_nfe = False
        self.valor_nfe = False
        self.natureza_nfe = ''
        self.descricao_objeto = ''
        self.valor_a_cobrar = 0.00

    def get_xml(self):

        xml = u'<nacional>'

        xml += u'<bairro_destinatario><![CDATA[%s]]></bairro_destinatario>' % \
               self.endereco.bairro
        xml += u'<cidade_destinatario><![CDATA[%s]]></cidade_destinatario>' % \
               self.endereco.cidade
        xml += u'<uf_destinatario>%s</uf_destinatario>' % self.endereco.uf
        xml += u'<cep_destinatario><![CDATA[%s]]></cep_destinatario>' % \
               self.endereco.cep
        xml += u'<codigo_usuario_postal>%s</codigo_usuario_postal>' % \
               self.codigo_usuario_postal
        xml += u'<centro_custo_cliente>%s</centro_custo_cliente>' % \
               self.centro_custo_cliente

        aux = str(self.num_nfe) if self.num_nfe else ''
        xml += u'<numero_nota_fiscal>%s</numero_nota_fiscal>' % aux

        aux = str(self.serie_nfe) if self.serie_nfe else ''
        xml += u'<serie_nota_fiscal>%s</serie_nota_fiscal>' % aux

        aux = str(self.valor_nfe) if self.valor_nfe else ''
        xml += u'<valor_nota_fiscal>%s</valor_nota_fiscal>' % aux

        xml += u'<natureza_nota_fiscal/>'
        xml += u'<descricao_objeto><![CDATA[%s]]></descricao_objeto>' % \
               self.descricao_objeto

        # aux = str(self.valor_a_cobrar) if self.valor_a_cobrar else ''
        xml += u'<valor_a_cobrar>1.2%f</valor_a_cobrar>' % self.valor_a_cobrar
        xml += u'</nacional>'

        self._validar_xml(xml)
        return xml


class TagNacionalPAC41068(TagNacional):

    def __init__(self, endereco, numero_nfe, serie_nfe):
        super(TagNacionalPAC41068, self).__init__(endereco)
        self.num_nfe = numero_nfe
        self.serie_nfe = serie_nfe
