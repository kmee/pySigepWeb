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

from tag_destinatario import TagDestinatario
from tag_nacional import TagNacional
from tag_dimensao_objeto import TagDimensaoObjeto
from etiqueta import Etiqueta
from servico_postagem import ServicoPostagem
from tag_servico_adicional import *
from tag_base import TagBase


class TagObjetoPostal(TagBase):

    def __init__(self, obj_destinatario, obj_nacional, obj_dimensao_objeto,
                 obj_servico_postagem, obj_servico_adicional, obj_etiqueta,
                 peso, status_processamento, codigo_objeto_cliente='',
                 cubagem=0.0000, numero_comprovante_de_postagem=0,
                 valor_cobrado=0.0, rt1='', rt2=''):

        self.destinatario = obj_destinatario
        self.nacional = obj_nacional
        self.dimensao_objeto = obj_dimensao_objeto
        self.servico_postagem = obj_servico_postagem
        self.servico_adicional = obj_servico_adicional
        self.etiqueta = obj_etiqueta
        self.codigo_objeto_cliente = codigo_objeto_cliente
        self.cubagem = cubagem
        self.peso = peso
        # self.data_postagem = date()
        self.status_processamento = status_processamento
        self.numero_comprovante_de_postagem = numero_comprovante_de_postagem
        self.valor_cobrado = valor_cobrado
        self.rt1 = rt1
        self.rt2 = rt2

    def get_xml(self):

        xml = u'<objeto_postal>\n'
        xml += u'<numero_etiqueta>%s</numero_etiqueta>\n' % \
               self.etiqueta.com_digito_verificador()
        xml += u'<codigo_objeto_cliente>%s</codigo_objeto_cliente>\n' % \
               self.codigo_objeto_cliente
        xml += u'<codigo_servico_postagem>%s</codigo_servico_postagem>\n' % \
               self.servico_postagem.codigo

        aux = str(self.cubagem) if self.cubagem else ''
        xml += u'<cubagem>%s</cubagem>\n' % aux

        xml += u'<peso>%d</peso>\n' % self.peso
        xml += u'<rt1>%s</rt1>\n' % self.rt1
        xml += u'<rt2>%s</rt2>\n' % self.rt2
        xml += self.destinatario.get_xml()
        xml += self.nacional.get_xml()
        xml += self.servico_adicional.get_xml()
        xml += self.dimensao_objeto.get_xml()
        xml += u'<data_postagem_sara></data_postagem_sara>\n'
        xml += u'<status_processamento>%s</status_processamento>\n' % \
               self.status_processamento

        aux = str(self.numero_comprovante_de_postagem) if \
            self.numero_comprovante_de_postagem else ''
        xml += u'<numero_comprovante_postagem>%s</numero_comprovante_postagem' \
               u'>\n' % aux

        aux = str(self.valor_cobrado) if self.valor_cobrado else ''
        xml += u'<valor_cobrado>%s</valor_cobrado>\n' % aux

        xml += u'</objeto_postal>\n'

        self._validar_xml(xml)
        return xml
