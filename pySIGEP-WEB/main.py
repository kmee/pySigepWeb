# -*- coding: utf-8 -*-
from model.servico_atende_cliente import ServicoAtendeCliente
from model.usuario import Usuario
from model.servico_postagem import ServicoPostagem
from model.ambiente import AmbienteHomologacao

sgpkey = {
    'usuario': 'sigep',
    'senha': 'n5f9t8',
    'cod_admin': '08082650',
    'contrato': '9912208555',
    'cartao': '0057018901',
    'numero_servico': '40216',
    'cep_origem': '70002900',
    'cep_destino': '74000100',
    'tipo_destinatario': 'C',
    'cnpj': '34028316000103',
    'quant_etiquetas': 1,
}


def main():
    print 'Iniciando'
    usr = Usuario('sigep', 'n5f9t8', '34028316000103', '08082650',
                  '9912208555', '0057018901')

    print usr.nome
    print usr.cartao_postagem

    l = [ServicoPostagem.SERVICO_CARTA_COMERCIAL_A_FATURAR,
         ServicoPostagem.SERVICO_PAC_41068]

    sv = ServicoAtendeCliente(ServicoAtendeCliente.AMBIENTE_HOMOLOGACAO)

    disp = sv.verifica_disponibilidade_servicos(l, '70002900', '74000100', usr)

    print disp

    print sv.consulta_cep('37503130').bairro

if __name__ == '__main__':
    main()

