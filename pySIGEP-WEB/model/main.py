# -*- coding: utf-8 -*-
from servico_atende_cliente import ServicoAtendeCliente
from usuario import Usuario
from servico_postagem import ServicoPostagem

from tag_plp import TagPLP
from tag_remetente import TagRemetente
from tag_destinatario import TagDestinatario
from tag_nacional import TagNacional
from tag_dimensao_objeto import TagDimensaoObjeto
from tag_servico_adicional import TagServicoAdicional
from servico_postagem import ServicoPostagem
from tag_objeto_postal import TagObjetoPostal
from tag_correios_log import TagCorreiosLog
from diretoria import Diretoria
from endereco import Endereco



def main():
    print 'Iniciando'
    usr = Usuario('sigep', 'n5f9t8', '34028316000103', '08082650',
                  '9912208555', '0057018901')

    print usr.nome
    print usr.num_cartao_postagem

    l = [ServicoPostagem.SERVICO_CARTA_COMERCIAL_A_FATURAR,
         ServicoPostagem.SERVICO_PAC_41068]

    sv = ServicoAtendeCliente(ServicoAtendeCliente.AMBIENTE_HOMOLOGACAO, usr)

    print sv.verifica_disponibilidade_servicos(l, '70002900', '74000100')
    print sv.consulta_cep('70002900').bairro
    print sv.consulta_status_cartao_postagem()

    sv_postagem = ServicoPostagem(ServicoPostagem.SERVICO_PAC_41068)
    etiquetas = sv.solicita_etiquetas(sv_postagem.servico_postagem_id,
                                      qtd_etiquetas=3)

    # etiquetas[0].etiqueta_sem_dig_verif = 'EC21325855 BR'
    # etiquetas[1].etiqueta_sem_dig_verif = 'EC21325856 BR'
    # etiquetas[2].etiqueta_sem_dig_verif = 'EC21325857 BR'

    digitos = sv.gera_digito_verificador_etiquetas(
        etiquetas, gerador=ServicoAtendeCliente.GERADOR_OFFLINE)

    for i in range(len(etiquetas)):
        print etiquetas[i].etiqueta_sem_dig_verif
        print digitos[i]

    usr_endereco = Endereco(logradouro='Avenida Central', numero=2370,
                            bairro='Centro', cep='70002900',
                            cidade='Brasilia', uf=Endereco.UF_PARANA,
                            complemento='sala 1205,12° andar')

    # Montando xml do plp
    obj_tag_plp = TagPLP(usr.num_cartao_postagem)
    obj_remetente = TagRemetente(usr.nome, usr.num_contrato, usr.codigo_admin,
                                 usr_endereco,
                                 Diretoria(Diretoria.DIRETORIA_DR_PARANA),
                                 telefone=6112345008, email='cli@mail.com.br')

    obj_destinatario = TagDestinatario('Destino Ltda')

    obj_postal = TagObjetoPostal()



     obj_destinatario, obj_destino_nacional,
                 obj_dimensao_objeto, obj_servico_postagem,
                 obj_servico_adicional, ob_etiqueta, peso, status_processamento):



if __name__ == '__main__':
    main()

