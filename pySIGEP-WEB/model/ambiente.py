# -*- coding: utf-8 -*-
from usuario import Usuario


class Ambiente(object):

    def __init__(self, dominio, url):
        self._dominio = dominio
        self._url = dominio + url

    @property
    def url(self):
        return self._url

    @property
    def dominio(self):
        return self._dominio


class AmbienteHomologacao(Ambiente):

    def __init__(self):
        super(AmbienteHomologacao, self).__init__(
            'https://apphom.correios.com.br',
            '/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl')

        self._usuario_homologacao = Usuario('sigep', 'n5f9t8',
                                            '34028316000103',  '08082650',
                                            '9912208555', '0057018901')

    @property
    def usuario_homogolacao(self):
        return self._usuario_homologacao


class AmbienteProducao(Ambiente):

    def __init__(self):
        super(AmbienteProducao, self).__init__(
            'https://apps.correios.com.br',
            '/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl')


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
        except KeyError as err:
            print u'[ERRO] Não existe ambiente com o nome fornecido! ' + err
