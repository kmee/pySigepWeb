# -*- coding: utf-8 -*-


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

