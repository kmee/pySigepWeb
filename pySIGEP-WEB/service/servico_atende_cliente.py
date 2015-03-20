# -*- coding: utf-8 -*-
from suds import WebFault


class ServicoAtendeCliente(object):

    def __init__(self):
        super(ServicoAtendeCliente, self).__init__()

    def verifica_disponibilidade_servico(self, lista_servicos, cep_origem,
                                         cep_destino, obj_usuario):

        str_servicos = ''

        for serv in lista_servicos:
            str_servicos += serv.codigo + ','

        try:
            disponibilidade = \
                self.servico.verificaDisponibilidadeServico(
                    obj_usuario.codigo_admin, str_servicos, cep_origem,
                    cep_destino, obj_usuario.nome, obj_usuario.senha)
        except WebFault as exp:
            print exp.message
