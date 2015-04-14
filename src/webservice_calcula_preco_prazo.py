# -*- coding: utf-8 -*-
from webservice_interface import *
from usuario import Usuario


class WebserviceCalculaPrecoPrazo(WebserviceInterface):

    _URL = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?WSDL'

    def __init__(self, obj_usuario):
        if not isinstance(obj_usuario, Usuario):
            raise TypeError

        self.obj_usuario = obj_usuario
        super(WebserviceCalculaPrecoPrazo, self).__init__(
            WebserviceCalculaPrecoPrazo._URL)

    @property
    def url(self):
        return WebserviceCalculaPrecoPrazo._URL

    def calcula_prazo(self):
        pass

    def calcula_preco(self):
        pass

    def calcula_preco_prazo(self, obj_servico_postagem, cep_origem,
                            cep_destino, peso, tipo_objeto, obj_dimensao,
                            usar_mao_propria, valor_declarado,
                            aviso_recebimento):
        try:
            result = self._service.CalcPrecoPrazo(
                self.obj_usuario.nome, self.obj_usuario.senha,
                obj_servico_postagem.codigo, cep_origem, cep_destino, peso,
                obj_dimensao, usar_mao_propria, valor_declarado,
                aviso_recebimento)
            return result
        except WebFault as exc:
            print '[ERRO] Em calcula_preco_prazo(). ' + exc.message
            return None
