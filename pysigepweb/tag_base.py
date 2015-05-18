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


class TagBase(object):

    XLM_SCHEMA = None

    def get_xml(self):
        raise NotImplementedError(u"[WARNING]Método deve ser sobreescrito!")

    def _validar_xml(self, xml):

        try:
            tree = etree.fromstring(xml.encode('utf8'))

            if self.XLM_SCHEMA is None:
                # xsd = open(sys.path[0] + '/pysigep_web/pysigepweb/data/plp_valid.xsd').read()
                xsd = get_xsd()
                schema_tree = etree.fromstring(xsd)
                self.XLM_SCHEMA = etree.XMLSchema(schema_tree)

            self.XLM_SCHEMA.assertValid(tree)

            print '[INFO] XML %s validado com sucesso!' % \
                  self.__class__.__name__

            return True

        except etree.XMLSyntaxError as e:
            print "[ERRO] Erro de parsing no xml", e
            print u'[ERRO] Validação de XML %s falhou!' % \
                  self.__class__.__name__
            return False

        except etree.DocumentInvalid as e:
            print '[ERRO] Erro validação XML fechaPLP', e
            print u'[ERRO] Validação de XML %s falhou!' % \
                  self.__class__.__name__
            return False

        except AssertionError as e:
            print "[ERRO] Documento Invalido", e
            print u'[ERRO] Validação de XML %s falhou!' % \
                  self.__class__.__name__
            return False
