# -*- coding: utf-8 -*-


class Ambiente(object):

    @property
    def url(self):
        pass


class AmbienteHomologacao(Ambiente):

    def __init__(self):
        super(AmbienteHomologacao, self).__init__()

    @property
    def url(self):
        return 'https://apphom.correios.com.br/SigepMasterJPA' \
               '/AtendeClienteService/AtendeCliente?wsdl'


class AmbienteProducao(Ambiente):

    def __init__(self):
        super(AmbienteProducao, self).__init__()

    @property
    def url(self):
        return 'https://apps.correios.com.br/SigepMasterJPA' \
               '/AtendeClienteService/AtendeCliente?wsdl'


class FabricaAmbiente(object):

    AMBIENTE_PRODUCAO = 'Producao'
    AMBIENTE_HOMOLOGACAO = 'Homologacao'

    _ambientes = {
        AMBIENTE_PRODUCAO: AmbienteProducao,
        AMBIENTE_HOMOLOGACAO: AmbienteHomologacao,
    }

    @staticmethod
    def get_ambiente(nome_ambiente):
            return FabricaAmbiente._ambientes[nome_ambiente]()
