# -*- coding: utf-8 -*-
from lxml import etree
import os, sys


class TagBase(object):

    XLM_SCHEMA = None

    def get_xml(self):
        raise NotImplementedError(u"[WARNING]Método deve ser sobreescrito!")

    def _validar_xml(self, xml):

        try:
            tree = etree.fromstring(xml.encode('utf8'))

            if self.XLM_SCHEMA is None:
                xsd = open(sys.path[0] +  '/pysigep_web/pysigepweb/data/plp_valid.xsd').read()
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
