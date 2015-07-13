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
from xml.etree.ElementTree import ElementTree, fromstring


class RespostaFechaPLPVariosServicos(object):

    def __init__(self, xml, id_plp_cliente):
        self._xml = xml
        self.id_plp_cliente = id_plp_cliente

    def salvar_xml(self, file_name):
        # tag raiz do xml
        root = fromstring(self.xml.encode('utf8'))
        # Cria backup do xml retornado
        ElementTree(root).write(file_name + '.xml')
        return True

    @property
    def xml(self):
        return self._xml