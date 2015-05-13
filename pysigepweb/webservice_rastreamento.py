# -*- coding: utf-8 -*-
import urllib
from resposta_rastreamento import *


class WebserviceRastreamento(object):
    _URL = 'http://websro.correios.com.br/sro_bin/sroii_xml.eventos'

    TIPO_LISTA_ETIQUETAS = 1
    TIPO_INTERVALO_ETIQUETAS = 2

    RETORNAR_TODOS_EVENTOS = 3
    RETORNAR_ULTIMO_EVENTO = 4

    _constantes = {
        TIPO_LISTA_ETIQUETAS: 'L',
        TIPO_INTERVALO_ETIQUETAS: 'F',
        RETORNAR_TODOS_EVENTOS: 'T',
        RETORNAR_ULTIMO_EVENTO: 'U',
    }

    def __init__(self):
        self.path = ''

    def rastrea_objetos(self, tipo, resultado, lista_etiquetas, cliente):

        etiquetas = ''
        for etq in lista_etiquetas:
            etiquetas += etq.com_digito_verificador()

        params = {
            "Usuario": cliente.login,
            "Senha": cliente.senha,
            'Tipo': WebserviceRastreamento._constantes[tipo],
            'Resultado': WebserviceRastreamento._constantes[resultado],
            'Objetos': etiquetas,
        }

        query = urllib.urlencode(params)
        f = urllib.urlopen(WebserviceRastreamento._URL, query)
        xml = f.read()
        f.close()

        return RespostaRastreamento(xml, etiquetas, self.path)
