# -*- coding: utf-8 -*-


class ServicoAdicional(object):

    AVISO_RECEBIMENTO: const <1>
    MAO_PROPRIA_NACIONAL: const <2>
    VALOR_DECLARADO_NACIONAL: const <19>
    REGISTRO_NACIONAL: const <25>
    AVISO_DE_RECEBIMENTO_DIGITAL: const <37>
    DEVOLUCAO_DE_NOTA_FISCAL_SEDEX: const <49>
    TAXA_DE_ENTREGA_DE_ENCOMENDA_DESPADRONIZADA: const <57>
    LOGISTICA_REVERSA_SIMULTANEA_DOMICILIARIA: const <67>
    LOGISTICA_REVERSA_SIMULTANEA_EM_AGENCIA: const <69>

    def __init__(self, codigo):
        self.codigo = codigo
