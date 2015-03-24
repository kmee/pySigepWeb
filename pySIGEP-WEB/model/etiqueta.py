# -*- coding: utf-8 -*-


class Etiqueta(object):

    def __init__(self, etiqueta_sem_dig_verif=''):
        self._etiqueta_com_dig_verif = ''
        self._etiqueta_sem_dig_verif = etiqueta_sem_dig_verif
        self._digito_verificador = 0

    @property
    def etiqueta_sem_dig_verif(self):
        return self._etiqueta_sem_dig_verif

    @etiqueta_sem_dig_verif.setter
    def etiqueta_sem_dig_verif(self, valor):
        self._etiqueta_sem_dig_verif = valor
        self._etiqueta_com_dig_verif = \
            valor.replace(' ', str(self._digito_verificador))

    @property
    def digito_verificador(self):
        return self._digito_verificador

    @digito_verificador.setter
    def digito_verificador(self, valor):
        self._digito_verificador = valor
        self._etiqueta_com_dig_verif = \
            self._etiqueta_sem_dig_verif.replace(' ', str(valor))

    @property
    def etiqueta_com_dig_verif(self):
        return self._etiqueta_com_dig_verif
