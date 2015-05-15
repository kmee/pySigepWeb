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


class Endereco(object):

    UF_ACRE = 'AC'
    UF_ALAGOAS = 'AL'
    UF_AMAZONAS = 'AM'
    UF_AMAPA = 'AP'
    UF_BAHIA = 'BA'
    UF_BRASILIA = 'DF'
    UF_CEARA = 'CE'
    UF_ESPIRITO_SANTO = 'ES'
    UF_GOIAS = 'GO'
    UF_MARANHAO = 'MA'
    UF_MINAS_GERAIS = 'MG'
    UF_MATO_GROSSO_DO_SUL = 'MS'
    UF_MATO_GROSSO = 'MT'
    UF_PARA = 'PA'
    UF_PARAIBA = 'PB'
    UF_PERNAMBUCO = 'PE'
    UF_PIAUI = 'PI'
    UF_PARANA = 'PR'
    UF_RIO_DE_JANEIRO = 'RJ'
    UF_RIO_GRANDE_DO_NORTE = 'RN'
    UF_RONDONIA = 'RO'
    UF_RORAIMA = 'RR'
    UF_RIO_GRANDE_DO_SUL = 'RS'
    UF_SANTA_CATARINA = 'SC'
    UF_SERGIPE = 'SE'
    UF_SAO_PAULO = 'SP'
    UF_TOCANTINS = 'TO'

    def __init__(self, logradouro, numero, bairro, cep, cidade, uf,
                 complemento=''):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
        self.complemento = complemento
