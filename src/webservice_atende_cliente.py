# -*- coding: utf-8 -*-
from webservice_interface import *
from ambiente import FabricaAmbiente
import plp_xml_validator
from usuario import Usuario


class WebserviceAtendeCliente(WebserviceInterface):

    AMBIENTE_PRODUCAO = FabricaAmbiente.AMBIENTE_PRODUCAO
    AMBIENTE_HOMOLOGACAO = FabricaAmbiente.AMBIENTE_HOMOLOGACAO

    GERADOR_ONLINE = True
    GERADOR_OFFLINE = False

    def __init__(self, nome_ambiente, obj_usuario):
        if not isinstance(obj_usuario, Usuario):
            raise TypeError

        self.obj_usuario = obj_usuario
        amb = FabricaAmbiente.get_ambiente(nome_ambiente)
        super(WebserviceAtendeCliente, self).__init__(amb.url)

    def verifica_disponibilidade_servicos(self, lista_servico_postagem,
                                          cep_origem, cep_destino):
        res = {}
        for sp in lista_servico_postagem:
            try:
                status = self._service.verificaDisponibilidadeServico(
                    self.obj_usuario.codigo_admin, sp.codigo, cep_origem,
                    cep_destino, self.obj_usuario.nome, self.obj_usuario.senha)

                res[sp.nome] = status
            except WebFault as exc:
                print exc.message
                print '[ERRO] Em verifica_disponibilidade_servicos(). ' +  \
                      exp.message

        return res

    def consulta_cep(self, cep):
        try:
            res = self._service.consultaCEP(cep)
            return res
        except WebFault as exc:
            print exc.message
            print '[ERRO] Em consulta_cep(). ' + exp.message
            return None

    def consulta_status_cartao_postagem(self):
        try:
            status = self._service.getStatusCartaoPostagem(
                self.obj_usuario.num_cartao_postagem, self.obj_usuario.nome,
                self.obj_usuario.senha)
            return status
        except WebFault as exc:
            print exc.message
            print '[ERRO] Em consulta_status_cartao_postagem(). ' + exp.message
            return None

    def solicita_etiquetas(self, servico_id, qtd_etiquetas=1,
                           tipo_destinatario='C'):
        try:
            faixa_etiquetas = self._service.solicitaEtiquetas(
                tipo_destinatario, self.obj_usuario.cnpj, servico_id,
                qtd_etiquetas, self.obj_usuario.nome, self.obj_usuario.senha)
        except WebFault as exc:
            print '[ERRO] Em solicita_etiquetas(). ' + exc.message
            return None

        from src.etiqueta import Etiqueta

        etiqueta_inicial = faixa_etiquetas.split(',')[0]
        etiqueta_numero = int(etiqueta_inicial[2:10])
        etiqueta_prefixo = etiqueta_inicial[0:2]
        etiqueta_sufixo = etiqueta_inicial[10:]

        etiquetas = []

        for i in range(qtd_etiquetas):
            valor = etiqueta_prefixo + str(etiqueta_numero + i).zfill(8) + \
                etiqueta_sufixo

            etiquetas.append(Etiqueta(valor))

        return etiquetas

    def gera_digito_verificador_etiquetas(self, lista_etiquetas,
                                          gerador=GERADOR_ONLINE):

        if gerador == WebserviceAtendeCliente.GERADOR_ONLINE:
            return self._gerador_online(lista_etiquetas)
        elif gerador == WebserviceAtendeCliente.GERADOR_OFFLINE:
            return self._gerador_offline(lista_etiquetas)
        else:
            print u'[ERRO] Opção de gerador inválida!'
            return []

    def _gerador_online(self, lista_etiquetas):
        etiquetas_sem_digito = []

        for etq in lista_etiquetas:
            etiquetas_sem_digito.append(etq.valor)

        try:
            dig_verif_list = self._service.geraDigitoVerificadorEtiquetas(
                etiquetas_sem_digito, self.obj_usuario.nome,
                self.obj_usuario.senha)
        except WebFault as exc:
            print '[ERRO] Em _gerador_online(). ' + exc.message
            return []

        return dig_verif_list

    @staticmethod
    def _gerador_offline(lista_etiquetas):
        from src.gerador_digito_verificador import GeradorDigitoVerificador

        dig_verif_list = []

        for i in range(len(lista_etiquetas)):
            dv = GeradorDigitoVerificador.gera_digito_verificador(
                lista_etiquetas[i].numero)
            dig_verif_list.append(dv)

        return dig_verif_list

    def fecha_plp_varios_servicos(self, obj_correios_log, id_plp_cliente,
                                  lista_obj_etiquetas):

        etiquetas_sem_digito = []
        for i in range(len(obj_correios_log.lista_objeto_postal)):
            # As etiquetas tem de ser enviadas sem o digito verificador
            # e sem o espaco em branco antes do sufixo da etiqueta
            etq = lista_obj_etiquetas[i].valor
            etiquetas_sem_digito.append(etq.replace(' ', ''))

        if plp_xml_validator.validate_xml(obj_correios_log.get_xml()):

            try:
                return self._service.fechaPlpVariosServicos(
                    obj_correios_log.get_xml(), id_plp_cliente,
                    self.obj_usuario.num_cartao_postagem, etiquetas_sem_digito,
                    self.obj_usuario.nome, self.obj_usuario.senha)
            except WebFault as exc:
                print '[ERRO] Em fecha_plp_varios_servicos(). ' + exc.message
                return None
