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

from lxml import etree
import os, sys
from xsd import *
from pysigep_exception import ErroValidacaoXML


class TagBase(object):

    XLM_SCHEMA = None

    def get_xml(self):
        raise NotImplementedError(u"[WARNING] Método deve ser sobreescrito!")

    def _validar_xml(self, xml):

        xml = xml.replace('\n', '')

        schema_tree = etree.fromstring(get_xsd())
        schema = etree.XMLSchema(schema_tree)

        source = etree.fromstring(xml.encode('utf8'))

        if schema.validate(source):
            print '[INFO] Validate XML %s sucessfull!' % \
                  self.__class__.__name__
            return True

        else:
            msg = '[ERRO] Validation of XML %s not sucessfull!' % \
                  self.__class__.__name__ + '\n'
            log = schema.error_log
            for error in iter(log):
                msg += "\n[ERROR]: " + error.message

            print msg
            raise ErroValidacaoXML(msg)
