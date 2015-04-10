# -*- coding: utf-8 -*-
from src import plp_xml_validator


class TagBase(object):

    def get_xml(self):
        raise NotImplementedError("Must subclass me")

    def _validar_xml(self, xml):

        if plp_xml_validator.validate_xml(xml):
            print '[INFO] XML %s validado com sucesso!' % \
                  self.__class__.__name__
        else:
            print u'[ERRO] Validação de XML %s falhou!' % \
                  self.__class__.__name__
