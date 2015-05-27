# -*- coding: utf-8 -*-
# #############################################################################
#
#    Brazillian Carrier Correios Sigep WEB
#    Copyright (C) 2015 KMEE (http://www.kmee.com.br)
#    @author: Michell Stuttgart <michell.stuttgarst@kmee.com.br>
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

from etiqueta import Etiqueta


class RespostaSolicitaIntervaloEtiquetas(object):

    def __init__(self, faixa_etiquetas, qtd_etiquetas):
        self._qtd_etiquetas = qtd_etiquetas
        self._faixa_etiquetas = faixa_etiquetas

    @property
    def faixa_etiquetas(self):
        return self._faixa_etiquetas

    @property
    def qtd_etiquetas(self):
        return self._qtd_etiquetas

    def gera_etiquetas(self):

        faixa_etiquetas = self._faixa_etiquetas

        etiqueta_inicial = faixa_etiquetas.split(',')[0]
        etiqueta_numero = int(etiqueta_inicial[2:10])
        etiqueta_prefixo = etiqueta_inicial[0:2]
        etiqueta_sufixo = etiqueta_inicial[11:]

        etiquetas = []

        for i in range(self._qtd_etiquetas):
            valor = etiqueta_prefixo + str(etiqueta_numero + i).zfill(8) + ' ' \
                                                                        + etiqueta_sufixo

            etiquetas.append(Etiqueta(valor))

        return etiquetas
