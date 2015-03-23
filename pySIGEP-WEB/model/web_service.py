# -*- coding: utf-8 -*-


class WebService(object):

    AMBIENTE_PRODUCAO = 'Producao'
    AMBIENTE_HOMOLOGACAO = 'Homologacao'

    SERVICO_ATENDE_CLIENTE = 'AtendeCliente'
    SERVICO_CALCULA_PRAZO_PRECO = 'CalculaPrecoPrazo'
    SERVICO_RASTREAMENTO = 'Rastreamento'

    WB_SIGEPWEB = {
        AMBIENTE_HOMOLOGACAO: 'https://apphom.correios.com.br/SigepMasterJPA'
                              '/AtendeClienteService/AtendeCliente?wsdl',
        AMBIENTE_PRODUCAO: 'https://apps.correios.com.br/SigepMasterJPA'
                           '/AtendeClienteService/AtendeCliente?wsdl',

    }

    AMBIENTE_HOMOLOGACAO_URL = \
        'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService' \
        '/AtendeCliente?wsdl'

    AMBIENTE_PRODUCAO_URL = 'https://apps.correios.com.br/SigepMasterJPA' \
                            '/AtendeClienteService/AtendeCliente?wsdl'


