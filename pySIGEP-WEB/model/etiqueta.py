# -*- coding: utf-8 -*-


class Etiqueta(object):

    def __init__(self, etiqueta_sem_dig_verif=''):
        self.etiqueta_com_dig_verif = ''
        self.etiqueta_sem_dig_verif = etiqueta_sem_dig_verif
        self.digito_verificador = 0

    @property
    def etiqueta_sem_dig_verif(self):
        return self.etiqueta_sem_dig_verif

    @etiqueta_sem_dig_verif.setter
    def etiqueta_sem_dig_verif(self, valor):
        self.etiqueta_sem_dig_verif = valor
        self.etiqueta_com_dig_verif = \
            valor.replace(' ', str(self.digito_verificador))

    @property
    def digito_verificador(self):
        return self.digito_verificador

    @digito_verificador.setter
    def digito_verificador(self, valor):
        self.digito_verificador = valor
        self.etiqueta_com_dig_verif = \
            self.etiqueta_sem_dig_verif.replace(' ', str(valor))
