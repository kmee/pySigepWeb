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

import urllib
from resposta_rastreamento import *


class WebserviceRastreamento(object):
    _URL = 'http://websro.correios.com.br/sro_bin/sroii_xml.eventos'

    TIPO_LISTA_ETIQUETAS = 1
    TIPO_INTERVALO_ETIQUETAS = 2

    RETORNAR_TODOS_EVENTOS = 3
    RETORNAR_ULTIMO_EVENTO = 4

    _constantes = {
        TIPO_LISTA_ETIQUETAS: 'L',
        TIPO_INTERVALO_ETIQUETAS: 'F',
        RETORNAR_TODOS_EVENTOS: 'T',
        RETORNAR_ULTIMO_EVENTO: 'U',
    }

    def __init__(self):
        self.path = ''

    def rastrea_objetos(self, tipo, resultado, lista_etiquetas, cliente):

        etiquetas = ''
        for etq in lista_etiquetas:
            etiquetas += etq.com_digito_verificador()

        # header para ser enviado ao webservice de rastreamento
        params = {
            "Usuario": cliente.login,
            "Senha": cliente.senha,
            'Tipo': WebserviceRastreamento._constantes[tipo],
            'Resultado': WebserviceRastreamento._constantes[resultado],
            'Objetos': etiquetas,
        }

        # Realizamos o rastreamento das etiquetas fornecidas
        query = urllib.urlencode(params)
        f = urllib.urlopen(WebserviceRastreamento._URL, query)
        xml = f.read()
        f.close()

        return RespostaRastreamento(xml, etiquetas, self.path)
