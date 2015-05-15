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


class RespostaCalculaPrecoPrazo(object):

    def __init__(self, returno_suds):

        self.codigo = returno_suds.Codigo
        self.valor = returno_suds.Valor
        self.prazo_entrega = returno_suds.PrazoEntrega
        self.valor_mao_propria = returno_suds.ValorMaoPropria
        self.valor_aviso_recebimento = returno_suds.ValorAvisoRecebimento
        self.valor_declarado = returno_suds.ValorValorDeclarado
        self.entrega_domiciliar = returno_suds.EntregaDomiciliar
        self.entrega_sabado = returno_suds.EntregaSabado
        self.erro = returno_suds.Erro
        self.msg_erro = returno_suds.MsgErro
        self.valor_sem_adicionais = returno_suds.ValorSemAdicionais
        self.obs_fim = returno_suds.obsFim

