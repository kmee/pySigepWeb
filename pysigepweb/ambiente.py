# -*- coding: utf-8 -*-


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
