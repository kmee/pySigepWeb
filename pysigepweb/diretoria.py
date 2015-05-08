# -*- coding: utf-8 -*-
from tag_base import TagBase


class Diretoria(TagBase):

    DIRETORIA_AC_ADMINISTRACAO_CENTRAL = 1
    DIRETORIA_DR_ACRE = 3
    DIRETORIA_DR_ALAGOAS = 4
    DIRETORIA_DR_AMAZONAS = 6
    DIRETORIA_DR_AMAPA = 5
    DIRETORIA_DR_BAHIA = 8
    DIRETORIA_DR_BRASILIA = 10
    DIRETORIA_DR_CEARA = 12
    DIRETORIA_DR_ESPIRITO_SANTO = 14
    DIRETORIA_DR_GOIAS = 16
    DIRETORIA_DR_MARANHAO = 18
    DIRETORIA_DR_MINAS_GERAIS = 20
    DIRETORIA_DR_MATO_GROSSO_DO_SUL = 22
    DIRETORIA_DR_MATO_GROSSO = 24
    DIRETORIA_DR_PARA = 28
    DIRETORIA_DR_PARAIBA = 30
    DIRETORIA_DR_PERNAMBUCO = 32
    DIRETORIA_DR_PIAUI = 34
    DIRETORIA_DR_PARANA = 36
    DIRETORIA_DR_RIO_DE_JANEIRO = 50
    DIRETORIA_DR_RIO_GRANDE_DO_NORTE = 60
    DIRETORIA_DR_RONDONIA = 26
    DIRETORIA_DR_RORAIMA = 65
    DIRETORIA_DR_RIO_GRANDE_DO_SUL = 64
    DIRETORIA_DR_SANTA_CATARINA = 68
    DIRETORIA_DR_SERGIPE = 70
    DIRETORIA_DR_SAO_PAULO_INTERIOR = 74
    DIRETORIA_DR_SAO_PAULO = 72
    DIRETORIA_DR_TOCANTINS = 75

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
        if codigo in Diretoria._diretorias:
            self._codigo = codigo
        else:
            print u'[AVISO] O codigo fornecido não é válido! Codigo: ', codigo
            self._codigo = False

    @property
    def descricao(self):
        return Diretoria._diretorias[self._codigo][0]

    @property
    def sigla(self):
        return Diretoria._diretorias[self._codigo][1]

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor in Diretoria._diretorias:
            raise KeyError
        self._codigo = valor

    def get_xml(self):
        return '<numero_diretoria>%d</numero_diretoria>' % self.codigo
