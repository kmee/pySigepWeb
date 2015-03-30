# -*- coding: utf-8 -*-
from src.servico_atende_cliente import ServicoAtendeCliente
from src.usuario import Usuario
from src.tag_plp import TagPLP
from src.tag_remetente import TagRemetente
from src.tag_dimensao_objeto import *
from src.tag_objeto_postal import *
from src.tag_correios_log import TagCorreiosLog
from src.diretoria import Diretoria
from src.endereco import Endereco


def main():

    usr = Usuario('sigep', 'n5f9t8', '34028316000103', '08082650',
                  '9912208555', '0057018901')

    l = [ServicoPostagem(ServicoPostagem.SERVICO_CARTA_COMERCIAL_A_FATURAR),
         ServicoPostagem(ServicoPostagem.SERVICO_PAC_41068)]

    print
    print u'[INFO] Iniciando Serviço de Atendimento ao Cliente'
    sv = ServicoAtendeCliente(ServicoAtendeCliente.AMBIENTE_HOMOLOGACAO, usr)

    print
    print u'[INFO] Verificando disponibilidades dos serviços:'
    for sp in l:
        print sp.nome

    print
    print '[INFO] Resultado da consulta para os cep %s (origem) e %s (' \
          'destino):' % ('70002900', '74000100')
    print '[INFO] Status da consulta:'
    print sv.verifica_disponibilidade_servicos(l, '70002900', '74000100')

    print
    print '[INFO] Consulta cep: %s' % '70002900'
    end_erp = sv.consulta_cep(70002900)
    print 'Bairro: ', end_erp.bairro
    print 'CEP:', end_erp.cep
    print 'Cidade: ', end_erp.cidade
    print 'Complemento: ', end_erp.complemento
    print 'Endereco: ', end_erp.end
    print 'Id:', end_erp.id
    print 'UF:', end_erp.uf

    print
    print u'[INFO] Verificando status do cartão de postagem'
    print sv.consulta_status_cartao_postagem()

    print
    sv_postagem = ServicoPostagem(ServicoPostagem.SERVICO_PAC_41068)

    print '[INFO] Solicitando etiquetas...'
    etiquetas = sv.solicita_etiquetas(sv_postagem.servico_postagem_id,
                                      qtd_etiquetas=3)

    for i in range(len(etiquetas)):
        print etiquetas[i].etiqueta_sem_dig_verif

    print '[INFO] Solicitando digito verificador para etiquetas...'
    print sv.gera_digito_verificador_etiquetas(
        etiquetas, gerador=ServicoAtendeCliente.GERADOR_OFFLINE)

    remetente_endereco = Endereco(logradouro='Avenida Central', numero=2370,
                                  bairro='Centro', cep=70002900,
                                  cidade='Brasilia', uf=Endereco.UF_PARANA,
                                  complemento=u'sala 1205,12° andar')

    destinatario_endereco = Endereco(logradouro='Avenida Central',
                                     numero=1065, bairro='Setor Industrial',
                                     cidade=u'Goiânia', uf=Endereco.UF_GOIAS,
                                     cep=74000100, complemento='Qd:102 A Lt:04')

    # Montando xml do plp
    print
    print '[INFO] Montando xml'
    obj_tag_plp = TagPLP(usr.num_cartao_postagem)
    obj_remetente = TagRemetente(usr.nome, usr.num_contrato, usr.codigo_admin,
                                 remetente_endereco,
                                 Diretoria(Diretoria.DIRETORIA_DR_PARANA),
                                 telefone=6112345008, email='cli@mail.com.br')

    obj_destinatario = TagDestinatario('Destino Ltda', destinatario_endereco,
                                       telefone=6212349644)

    obj_nacional = TagNacional(endereco=destinatario_endereco,
                               numero_nfe=102030, valor_a_cobrar=0.00,
                               serie_nfe='1')

    obj_servico_adicional = TagServicoAdicional(99.00)

    obj_servico_adicional.add_tipo_servico_adicional(
        TagServicoAdicional.TIPO_AVISO_RECEBIMENTO)

    obj_servico_adicional.add_tipo_servico_adicional(
        TagServicoAdicional.TIPO_VALOR_DECLARADO)

    obj_dimensao_objeto = TagDimensaoObjeto(Caixa(20, 30, 38))

    obj_postal = TagObjetoPostal(obj_destinatario=obj_destinatario,
                                 obj_nacional=obj_nacional,
                                 obj_dimensao_objeto=obj_dimensao_objeto,
                                 obj_servico_adicional=obj_servico_adicional,
                                 obj_servico_postagem=sv_postagem,
                                 ob_etiqueta=etiquetas[0],
                                 peso=200, status_processamento=0)

    obj_correios_log = TagCorreiosLog('2.3', obj_tag_plp, obj_remetente,
                                      [obj_postal])

    print
    print u'[INFO] Fecha plp para varios serviços'
    print
    plp = sv.fecha_plp_varios_servicos(obj_correios_log, long(123), etiquetas)
    print
    print '[INFO] Novo PLP id: ', plp

if __name__ == '__main__':
    main()

