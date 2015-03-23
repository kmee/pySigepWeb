# -*- coding: utf-8 -*-
from suds import WebFault

from interface_servico import InterfaceServico
from ambiente import FabricaAmbiente
from consulta_cep_resposta import ConsultaCEPResposta

class ServicoAtendeCliente(InterfaceServico):

    AMBIENTE_PRODUCAO = FabricaAmbiente.AMBIENTE_PRODUCAO
    AMBIENTE_HOMOLOGACAO = FabricaAmbiente.AMBIENTE_HOMOLOGACAO

    def __init__(self, nome_ambiente):
        amb = FabricaAmbiente.get_ambiente(nome_ambiente)
        super(ServicoAtendeCliente, self).__init__(amb.url)

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

    def consulta_cep(self, cep):

        if not isinstance(cep, str):
            raise TypeError

        try:
            res = self.servico.consultaCEP(cep)
            return ConsultaCEPResposta(res.bairro, res.cep, res.end,
                                       res.id, res.uf, res.complemento,
                                       res.complemento2)

        except WebFault as exp:
            print exp.message
            return None




