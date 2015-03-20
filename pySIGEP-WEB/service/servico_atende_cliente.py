# -*- coding: utf-8 -*-
from suds import WebFault


class ServicoAtendeCliente(object):

    def __init__(self):
        super(ServicoAtendeCliente, self).__init__()

    def verifica_disponibilidade_servicos(self, lista_codigo_servicos,
                                          cep_origem, cep_destino, obj_usuario):

        if not isinstance(lista_codigo_servicos, list):
            raise TypeError

        res = {}

        for codigo in lista_codigo_servicos:
            try:
                res[codigo] = self.servico.verificaDisponibilidadeServico(
                    obj_usuario.codigo_admin, codigo, cep_origem,
                    cep_destino, obj_usuario.nome, obj_usuario.senha)
            except WebFault as exp:
                print exp.message

        return res

    def verifica_disponibilidade_servico(self, codigo_servico, cep_origem,
                                         cep_destino, obj_usuario):

        if not isinstance(codigo_servico, str):
            raise TypeError

        try:
            res = self.servico.verificaDisponibilidadeServico(
                obj_usuario.codigo_admin, codigo_servico, cep_origem,
                cep_destino, obj_usuario.nome, obj_usuario.senha)
        except WebFault as exp:
            print exp.message

        return res








