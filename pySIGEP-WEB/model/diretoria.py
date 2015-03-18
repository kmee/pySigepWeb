# -*- coding: utf-8 -*-

DIRETORIA_AC_ADMINISTRACAO_CENTRAL = '00001'
DIRETORIA_DR_ACRE = '00003'
DIRETORIA_DR_ALAGOAS = '00004'
DIRETORIA_DR_AMAZONAS = '00006'
DIRETORIA_DR_AMAPA = '00005'
DIRETORIA_DR_BAHIA = '00008'
DIRETORIA_DR_BRASILIA = '00010'
DIRETORIA_DR_CEARA = '00012'
DIRETORIA_DR_ESPIRITO_SANTO = '00014'
DIRETORIA_DR_GOIAS = '00016'
DIRETORIA_DR_MARANHAO = '00018'
DIRETORIA_DR_MINAS_GERAIS = '00020'
DIRETORIA_DR_MATO_GROSSO_DO_SUL = '00022'
DIRETORIA_DR_MATO_GROSSO = '00024'
DIRETORIA_DR_PARA = '00028'
DIRETORIA_DR_PARAIBA = '00030'
DIRETORIA_DR_PERNAMBUCO = '00032'
DIRETORIA_DR_PIAUI = '00034'
DIRETORIA_DR_PARANA = '00036'
DIRETORIA_DR_RIO_DE_JANEIRO = '00050'
DIRETORIA_DR_RIO_GRANDE_DO_NORTE = '00060'
DIRETORIA_DR_RONDONIA = '00026'
DIRETORIA_DR_RORAIMA = '00065'
DIRETORIA_DR_RIO_GRANDE_DO_SUL = '00064'
DIRETORIA_DR_SANTA_CATARINA = '00068'
DIRETORIA_DR_SERGIPE = '00070'
DIRETORIA_DR_SAO_PAULO_INTERIOR = '00074'
DIRETORIA_DR_SAO_PAULO = '00072'
DIRETORIA_DR_TOCANTINS = '00075'


class Diretoria(object):

    _diretorias = {
        DIRETORIA_AC_ADMINISTRACAO_CENTRAL: ('AC', u'AC Administraçao Central'),
        DIRETORIA_DR_ACRE: ('ACR', 'DR - Acre'),
        DIRETORIA_DR_ALAGOAS: ('AL', 'DR - Alagoas'),
        DIRETORIA_DR_AMAZONAS: ('AM', 'DR - Amazonas'),
        DIRETORIA_DR_AMAPA: ('AP', u'DR - Amapá'),
        DIRETORIA_DR_BAHIA: ('BA', 'DR - Bahia'),
        DIRETORIA_DR_BRASILIA: ('BSB', u'DR - Brasília'),
        DIRETORIA_DR_CEARA: ('CE', u'DR - Ceará'),
        DIRETORIA_DR_ESPIRITO_SANTO: ('ES', u'DR - Espírito Santo'),
        DIRETORIA_DR_GOIAS: ('GO', u'DR - Goiás'),
        DIRETORIA_DR_MARANHAO: ('MA', u'DR - Maranhão'),
        DIRETORIA_DR_MINAS_GERAIS: ('MG', 'DR - Minas Gerais'),
        DIRETORIA_DR_MATO_GROSSO_DO_SUL: ('MS', 'DR - Mato Grosso do Sul'),
        DIRETORIA_DR_MATO_GROSSO: ('MT', 'DR - Mato Grosso'),
        DIRETORIA_DR_PARA: ('PA', u'DR - Pará'),
        DIRETORIA_DR_PARAIBA: ('PB', u'DR - Paraíba'),
        DIRETORIA_DR_PERNAMBUCO: ('PE', 'DR - Pernambuco'),
        DIRETORIA_DR_PIAUI: ('PI', u'DR - Piauí'),
        DIRETORIA_DR_PARANA: ('PR', u'DR - Paraná'),
        DIRETORIA_DR_RIO_DE_JANEIRO: ('RJ', 'DR - Rio de Janeiro'),
        DIRETORIA_DR_RIO_GRANDE_DO_NORTE: ('RN', 'DR - Rio Grande do Norte'),
        DIRETORIA_DR_RONDONIA: ('RO', 'DR - Rondonia'),
        DIRETORIA_DR_RORAIMA: ('RR', 'DR - Roraima'),
        DIRETORIA_DR_RIO_GRANDE_DO_SUL: ('RS', 'DR - Rio Grande do Sul'),
        DIRETORIA_DR_SANTA_CATARINA: ('SC', 'DR - Santa Catarina'),
        DIRETORIA_DR_SERGIPE: ('SE', 'DR - Sergipe'),
        DIRETORIA_DR_SAO_PAULO_INTERIOR: ('SPI', u'DR - São Paulo Interior'),
        DIRETORIA_DR_SAO_PAULO: ('SPM', u'DR - São Paulo'),
        DIRETORIA_DR_TOCANTINS: ('TO', 'DR - Tocantins'),
    }

    def __init__(self, codigo):
        self.codigo = codigo

    @property
    def descricao(self):
        return self._diretorias[self.codigo][0]

    @property
    def sigla(self):
        return self._diretorias[self.codigo][1]

    @property
    def codigo(self):
        return self.codigo

    @codigo.setter
    def codigo(self, valor):
        if valor in self._diretorias:
            raise KeyError
        self.codigo = valor





