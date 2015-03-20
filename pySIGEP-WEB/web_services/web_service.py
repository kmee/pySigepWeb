# -*- coding: utf-8 -*-

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