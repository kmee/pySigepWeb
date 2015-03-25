# -*- coding: utf-8 -*-
from model.servico_atende_cliente import ServicoAtendeCliente
from model.usuario import Usuario
from model.servico_postagem import ServicoPostagem


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
    print sv.consulta_cep('37503130').bairro
    print sv.consulta_status_cartao_postagem()

    sv_postagem = ServicoPostagem(ServicoPostagem.SERVICO_PAC_41068)
    etiquetas = sv.solicita_etiquetas(sv_postagem.servico_postagem_id,
                                      qtd_etiquetas=3)

    etiquetas[0].etiqueta_sem_dig_verif = 'EC21325855 BR'
    etiquetas[1].etiqueta_sem_dig_verif = 'EC21325856 BR'
    etiquetas[2].etiqueta_sem_dig_verif = 'EC21325857 BR'

    digitos = sv.gera_digito_verificador_etiquetas(etiquetas,
                                                   gerador=ServicoAtendeCliente.GERADOR_OFFLINE)

    for i in range(len(etiquetas)):
        print etiquetas[i].etiqueta_sem_dig_verif
        print digitos[i]

if __name__ == '__main__':
    main()

