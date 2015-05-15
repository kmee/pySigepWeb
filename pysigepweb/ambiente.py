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


class Ambiente(object):

    @property
    def url(self):
        pass


class AmbienteHomologacao(Ambiente):

    _URL_HOMOLOGACAO = 'https://apphom.correios.com.br/' \
                       'SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'

    def __init__(self):
        super(AmbienteHomologacao, self).__init__()

    @property
    def url(self):
        return AmbienteHomologacao._URL_HOMOLOGACAO


class AmbienteProducao(Ambiente):

    _URL_PRODUCAO = 'https://apps.correios.com.br/SigepMasterJPA' \
                    '/AtendeClienteService/AtendeCliente?wsdl'

    def __init__(self):
        super(AmbienteProducao, self).__init__()

    @property
    def url(self):
        return AmbienteProducao._URL_PRODUCAO


class FabricaAmbiente(object):

    AMBIENTE_PRODUCAO = 'Producao'
    AMBIENTE_HOMOLOGACAO = 'Homologacao'

    _ambientes = {
        AMBIENTE_PRODUCAO: AmbienteProducao,
        AMBIENTE_HOMOLOGACAO: AmbienteHomologacao,
    }

    @staticmethod
    def get_ambiente(nome_ambiente):
        try:
            return FabricaAmbiente._ambientes[nome_ambiente]()
        except KeyError as exc:
            exit(u'[ERRO] Não existe Ambiente com o nome fornecido: \"%s\"' \
                 % exc.message)
