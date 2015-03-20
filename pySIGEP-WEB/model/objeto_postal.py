# -*- coding: utf-8 -*-
from destinatario import Destinatario
from destino_nacional import DestinoNacional
from dimensao_objeto import DimensaoObjeto
from etiqueta import Etiqueta
from servico_postagem import ServicoPostagem
from servico_adicional import ServicoAdicional
from datetime import date


class ObjetoPostal(object):

    def __init__(self, obj_destinatario, obj_destino_nacional,
                 obj_dimensao_objeto, obj_servico_postagem,
                 obj_servico_adicional):

        if not isinstance(obj_destinatario, Destinatario):
            raise TypeError

        self.destinatario = obj_destinatario

        if not isinstance(obj_destinatario, Destinatario):
            raise TypeError

        self.destino_nacional = obj_destino_nacional

        if not isinstance(obj_destino_nacional, DestinoNacional):
            raise TypeError

        self.dimensao_objeto = obj_dimensao_objeto

        if not isinstance(obj_dimensao_objeto, DimensaoObjeto):
            raise TypeError

        self.servico_postagem = obj_servico_postagem

        if not isinstance(obj_servico_postagem, ServicoPostagem):
            raise TypeError

        self.servico_adicional = obj_servico_adicional

        if not isinstance(obj_servico_adicional, ServicoAdicional):
            raise TypeError

        self.etiquetas = []
        self.cubagem = 0.0
        self.peso = 0.0
        # self.data_postagem = date()
        self.status_processamento = ''
        self.valor_cobrado = 0.0

    @staticmethod
    def obj_validate(obj, obj_class):
        if not isinstance(obj, obj_class):
            raise TypeError

    def add_etiqueta(self, etq):
        if not isinstance(etq, Etiqueta):
            raise TypeError
        self.etiquetas.append(etq)

