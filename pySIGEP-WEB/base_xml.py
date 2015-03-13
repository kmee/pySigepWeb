# -*- coding: utf-8 -*-


class BaseXML(object):

    def __init__(self):
        self._valor = None

    def xml(self):
        pass

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

