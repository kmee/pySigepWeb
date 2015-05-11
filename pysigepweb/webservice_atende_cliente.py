# -*- coding: utf-8 -*-
from webservice_interface import *
from ambiente import FabricaAmbiente
from resposta_busca_cliente import *
from resposta_fecha_plp_varios_servicos import ResposaFechaPLPVariosServicos
from etiqueta import Etiqueta


class WebserviceAtendeCliente(WebserviceInterface):

    AMBIENTE_PRODUCAO = FabricaAmbiente.AMBIENTE_PRODUCAO
    AMBIENTE_HOMOLOGACAO = FabricaAmbiente.AMBIENTE_HOMOLOGACAO

    def __init__(self, nome_ambiente, obj_usuario):
        self.obj_usuario = obj_usuario
        amb = FabricaAmbiente.get_ambiente(nome_ambiente)
        super(WebserviceAtendeCliente, self).__init__(amb.url)

    @staticmethod
    def _formata_cep(cep):
        return cep.replace('-', '')

    def verifica_disponibilidade_servicos(self, lista_servico_postagem,
                                          cep_origem, cep_destino):

        cep_origem_form = self._formata_cep(cep_origem)
        cep_destino_form = self._formata_cep(cep_destino)

        if len(cep_origem_form) != 8:
            msg = 'CEP Origem %s com numero incorreto de caracteres. Valor ' \
                  'correto deve ser 8.' % cep_origem
            raise ErroTamanhoParamentroIncorreto(msg)

        if len(cep_destino_form) != 8:
            msg = 'CEP Destino %s com numero incorreto de caracteres. Valor ' \
                  'correto deve ser 8.' % cep_destino
            raise ErroTamanhoParamentroIncorreto(msg)

        res = {}
        for sp in lista_servico_postagem:
            try:
                status = self._service.verificaDisponibilidadeServico(
                    self.obj_usuario.codigo_admin, sp.codigo, cep_origem_form,
                    cep_destino_form, self.obj_usuario.nome,
                    self.obj_usuario.senha)

                res[sp.nome] = status
            except WebFault as e:
                raise ErroConexaoComServidor(e.message)

        return res

    def busca_cliente(self):

        try:
            result = self._service.buscaCliente(
                self.obj_usuario.num_contrato,
                self.obj_usuario.num_cartao_postagem,
                self.obj_usuario.nome,
                self.obj_usuario.senha)

            rbc = RespostaBuscaCliente(result.nome,
                                       result.cnpj,
                                       result.descricaoStatusCliente)

            for contrato in result.contratos:

                ct = Contrato(contrato.codigoDiretoria,
                              contrato.contratoPK.numero)

                for cartao_postagem in contrato.cartoesPostagem:

                    cp = CartaoPostagem(cartao_postagem.statusCartaoPostagem,
                                        cartao_postagem.codigoAdministrativo,
                                        cartao_postagem.numero)

                    for servico in cartao_postagem.servicos:
                        cp.add_servico_postagem(servico.codigo,
                                                servico.descricao,
                                                servico.id)

                    ct.cartoes_postagem.append(cp)

                rbc.contratos.append(ct)

            return rbc

        except WebFault as e:
            raise ErroConexaoComServidor(e.message)

    def consulta_cep(self, cep):

        if len(cep) != 8:
            msg = 'CEP fornecido com numero incorreto de digitos. Valor ' \
                  'correto' \
                  ' deve ser 8.'
            raise ErroTamanhoParamentroIncorreto(msg)

        try:
            res = self._service.consultaCEP(cep)
            return res
        except WebFault as e:
            raise ErroConexaoComServidor(e.message)

    def consulta_status_cartao_postagem(self, num_cartao):
        try:
            return self._service.getStatusCartaoPostagem(
                num_cartao, self.obj_usuario.nome, self.obj_usuario.senha)
        except WebFault as e:
            raise ErroConexaoComServidor(e.message)

    def solicita_etiquetas(self, servico_id, qtd_etiquetas=1,
                           tipo_destinatario='C'):
        try:
            faixa_etiquetas = self._service.solicitaEtiquetas(
                tipo_destinatario, self.obj_usuario.cnpj, servico_id,
                qtd_etiquetas, self.obj_usuario.nome, self.obj_usuario.senha)
        except WebFault as e:
            raise ErroConexaoComServidor(e.message)

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
                                          online=True):

        if online:
            return self._gerador_online(lista_etiquetas)
        else:
            return self._gerador_offline(lista_etiquetas)

    def _gerador_online(self, lista_etiquetas):
        etiquetas_sem_digito = []

        for etq in lista_etiquetas:
            etiquetas_sem_digito.append(etq.valor)

        try:
            dig_verif_list = self._service.geraDigitoVerificadorEtiquetas(
                etiquetas_sem_digito, self.obj_usuario.nome,
                self.obj_usuario.senha)
        except WebFault as exc:
            raise ErroConexaoComServidor(exc.message)

        return dig_verif_list

    @staticmethod
    def _gerador_offline(lista_etiquetas):

        dig_verif_list = []
        multiplicadores = [8, 6, 4, 2, 3, 5, 9, 7]

        for etq in lista_etiquetas:

            soma = 0

            if len(etq.numero) != 8:
                dv = u'[Erro] Número de digito deve ser 8'
            else:
                for i in range(8):
                    soma += int(etq.numero[i:(i+1)]) * multiplicadores[i]

                resto = soma % 11
                if resto == 0:
                    dv = '5'
                elif resto == 1:
                    dv = '0'
                else:
                    dv = str(11 - resto)

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

        # if plp_xml_validator.validate_xml(obj_correios_log.get_xml()):

        xml = obj_correios_log.get_xml()

        if xml:
            try:
                id_plp_cliente = self._service.fechaPlpVariosServicos(
                    xml, id_plp_cliente, self.obj_usuario.num_cartao_postagem,
                    etiquetas_sem_digito, self.obj_usuario.nome,
                    self.obj_usuario.senha)

                return ResposaFechaPLPVariosServicos(xml, id_plp_cliente)

            except WebFault as exc:
                raise ErroConexaoComServidor(exc.message)
