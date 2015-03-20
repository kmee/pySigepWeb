# -*- coding: utf-8 -*-
from suds import WebFault
from interface_servico import InterfaceServico


class ServicoAtendeCliente(InterfaceServico):

    def __init__(self):
        url = 'https://apphom.correios.com.br/SigepMasterJPA' \
              '/AtendeClienteService/AtendeCliente?wsdl'
        super(ServicoAtendeCliente, self).__init__(url)

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



