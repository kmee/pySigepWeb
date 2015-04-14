# -*- coding: utf-8 -*-


class RespostaCalculaPrecoPrazo(object):

    def __init__(self, codigo, valor, prazo_entrega, valor_mao_propria,
                 valor_aviso_recebimento, valor_valor_declarado,
                 entrega_domiciliar, entrega_sabado, erro, msg_erro,
                 valor_sem_adicionais, obs_fim):

        self.codigo = codigo
        self.valor = valor
        self.prazo_entrega = prazo_entrega
        self.valor_mao_propria = valor_mao_propria
        self.valor_aviso_recebimento = valor_aviso_recebimento
        self.valor_declarado = valor_valor_declarado
        self.entrega_domiciliar = entrega_domiciliar
        self.entrega_sabado = entrega_sabado
        self.erro = erro
        self.msg_erro = msg_erro
        self.valor_sem_adicionais = valor_sem_adicionais
        self.obs_fim = obs_fim
