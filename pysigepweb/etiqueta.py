# -*- coding: utf-8 -*-


class Etiqueta(object):

    def __init__(self, etiqueta_sem_dig_verif):

        if len(etiqueta_sem_dig_verif) != 13:
            print '[AVISO] Etiqueta com tamanho incorreto.',

        self._valor = etiqueta_sem_dig_verif
        self._digito_verificador = False
        self._numero = etiqueta_sem_dig_verif[2:10]
        self._prefixo = etiqueta_sem_dig_verif[0:2]
        self._sufixo = etiqueta_sem_dig_verif[10:]

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, etiqueta_sem_dig_verif):

        if len(etiqueta_sem_dig_verif) != 13:
            print '[AVISO] Etiqueta com tamanho incorreto. ', \
                etiqueta_sem_dig_verif

        self._valor = etiqueta_sem_dig_verif
        self._numero = etiqueta_sem_dig_verif[2:10]
        self._prefixo = etiqueta_sem_dig_verif[0:2]
        self._sufixo = etiqueta_sem_dig_verif[10:]

    @property
    def digito_verificador(self):
        return self._digito_verificador

    @digito_verificador.setter
    def digito_verificador(self, valor):
        self._digito_verificador = valor

    @property
    def sufixo(self):
        return self._sufixo

    @property
    def prefixo(self):
        return self._prefixo

    @property
    def numero(self):
        return self._numero

    def com_digito_verificador(self):
        etq = self._valor
        if self.digito_verificador:
            etq = etq.replace(' ', str(self.digito_verificador))
        return etq

