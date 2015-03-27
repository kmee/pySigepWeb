# -*- coding: utf-8 -*-


class Endereco(object):

    UF_ACRE = 'AC'
    UF_ALAGOAS = 'AL'
    UF_AMAZONAS = 'AM'
    UF_AMAPA = 'AP'
    UF_BAHIA = 'BA'
    UF_BRASILIA = 'DF'
    UF_CEARA = 'CE'
    UF_ESPIRITO_SANTO = 'ES'
    UF_GOIAS = 'GO'
    UF_MARANHAO = 'MA'
    UF_MINAS_GERAIS = 'MG'
    UF_MATO_GROSSO_DO_SUL = 'MS'
    UF_MATO_GROSSO = 'MT'
    UF_PARA = 'PA'
    UF_PARAIBA = 'PB'
    UF_PERNAMBUCO = 'PE'
    UF_PIAUI = 'PI'
    UF_PARANA = 'PR'
    UF_RIO_DE_JANEIRO = 'RJ'
    UF_RIO_GRANDE_DO_NORTE = 'RN'
    UF_RONDONIA = 'RO'
    UF_RORAIMA = 'RR'
    UF_RIO_GRANDE_DO_SUL = 'RS'
    UF_SANTA_CATARINA = 'SC'
    UF_SERGIPE = 'SE'
    UF_SAO_PAULO = 'SP'
    UF_TOCANTINS = 'TO'

    def __init__(self, logradouro, numero, bairro, cep, cidade, uf,
                 complemento=''):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
        self.complemento = complemento
