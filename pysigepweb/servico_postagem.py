# -*- coding: utf-8 -*-


class ServicoPostagem(object):

    SERVICO_SEDEX_10 = 40215
    SERVICO_E_SEDEX_STANDARD = 81019
    SERVICO_CARTA_COMERCIAL_A_FATURAR = 10065
    SERVICO_PAC_41068 = 41068
    SERVICO_SEDEX_CONTRATO_40444 = 40444
    SERVICO_SEDEX_CONTRATO_40436 = 40436
    SERVICO_SEDEX_CONTRATO_40096 = 40096
    SERVICO_SEDEX_REVERSO_40096 = 40380
    SERVICO_SEDEX_A_VISTA = 40010
    SERVICO_PAC_CONTRATO_41211 = 41211
    SERVICO_SEDEX_PAGAMENTO_NA_ENTREGA = 40630
    SERVICO_SEDEX_AGRUPADO_II = 40916
    SERVICO_SEDEX_AGRUPADO_I = 40908
    SERVICO_PAC_GRANDES_FORMATOS = 41300
    SERVICO_SEDEX_12 = 40169
    SERVICO_SEDEX_HOJE_40290 = 40290
    SERVICO_CARTA_COMERCIAL_REGISTRADA = 10154
    SERVICO_PROTOCOLO_POSTAL = 40150

    SERVICO_PAC_41106 = 41106
    SERVICO_SEDEX_10_PACOTE = 40886
    SERVICO_SEDEX_HOJE_40878 = 40878
    SERVICO_SEDEX_VAREJO_A_COBRAR = 40045

    _servicos = {
        SERVICO_PAC_41068: ('Pac 41068', 109819),
        SERVICO_PAC_41106: ('Pac 41106', 110353),
        SERVICO_PAC_GRANDES_FORMATOS: ('Pac Grandes Formatos', 120366),
        SERVICO_PAC_CONTRATO_41211: ('Pac Contrato', 162149),
        SERVICO_E_SEDEX_STANDARD: ('E-Sedex Standard', 104672),
        SERVICO_SEDEX_CONTRATO_40096: ('Sedex 40096', 104625),
        SERVICO_SEDEX_CONTRATO_40436: ('Sedex 40436', 109810),
        SERVICO_SEDEX_CONTRATO_40444: ('Sedex 40444', 109811),
        SERVICO_SEDEX_12: ('Sedex 12', 115218),
        SERVICO_SEDEX_10: ('Sedex 10', 104707),
        SERVICO_SEDEX_10_PACOTE: ('Sedex 10 Pacote', None),
        SERVICO_SEDEX_HOJE_40290: ('Sedex Hoje 40290', 108934),
        SERVICO_SEDEX_HOJE_40878: ('Sedex Hoje 40878', None),
        SERVICO_SEDEX_A_VISTA: ('Sedex a vista', 104295),
        SERVICO_SEDEX_VAREJO_A_COBRAR: ('Sedex Varejo a Cobrar', None),
        SERVICO_SEDEX_AGRUPADO_I: ('Sedex Agrupado', 119461),
        SERVICO_SEDEX_AGRUPADO_II: ('Sedex Agrupado II', 118568),
        SERVICO_SEDEX_REVERSO_40096: ('Sedex Reverso', 109806),
        SERVICO_PROTOCOLO_POSTAL: ('Protocolo Postal', 115136),
        SERVICO_SEDEX_PAGAMENTO_NA_ENTREGA: ('Sedex Pagamento na Entrega',
                                             114976),
        SERVICO_CARTA_COMERCIAL_A_FATURAR: ('Carta Comercial a Faturar',
                                            109480),
        SERVICO_CARTA_COMERCIAL_REGISTRADA: ('Carta Comercial Registrada',
                                             116985),
    }

    def __init__(self, codigo, nome, servico_id):
        self._codigo = codigo

        if codigo in ServicoPostagem._servicos:
            self._nome = ServicoPostagem._servicos[codigo][0]
        else:
            self._nome = nome
        self._servico_postagem_id = servico_id

    @property
    def nome(self):
        return self._nome

    @property
    def servico_postagem_id(self):
        return self._servico_postagem_id

    @property
    def codigo(self):
        return self._codigo

    # @codigo.setter
    # def codigo(self, valor):
    #     if valor not in self._servicos:
    #         raise KeyError
    #     self._codigo = valor
    #     self._nome = self._servicos[self.codigo][0]
    #     self._servico_postagem_id = self._servicos[self.codigo][1]
