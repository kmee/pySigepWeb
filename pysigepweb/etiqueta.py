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

from pysigep_exception import ErroTamanhoParamentroIncorreto


class Etiqueta(object):

    def __init__(self, etiqueta_sem_dig_verif):

        if len(etiqueta_sem_dig_verif) != 13:
            print '[AVISO] Etiqueta com tamanho incorreto.',

        self._digito_verificador = None
        self._numero = etiqueta_sem_dig_verif[2:10]
        self._prefixo = etiqueta_sem_dig_verif[0:2]
        self._sufixo = etiqueta_sem_dig_verif[11:]
        self._valor = self._prefixo + self._numero + ' ' + self._sufixo

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, etiqueta_sem_dig_verif):

        if len(etiqueta_sem_dig_verif) != 13:
            aux = '[AVISO] Etiqueta com tamanho incorreto: %s' % \
                  etiqueta_sem_dig_verif
            raise ErroTamanhoParamentroIncorreto(aux)

        # self._valor = etiqueta_sem_dig_verif
        self._numero = etiqueta_sem_dig_verif[2:10]
        self._prefixo = etiqueta_sem_dig_verif[0:2]
        self._sufixo = etiqueta_sem_dig_verif[11:]
        self._valor = self._prefixo + self._numero + ' ' + self._sufixo

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
        if self.digito_verificador is not None:
            etq = etq.replace(' ', str(self.digito_verificador))
        return etq

