# -*- coding: utf-8 -*-

import unittest
import os
import sys

from pysigepweb.webservice_atende_cliente import WebserviceAtendeCliente

from pysigepweb.webservice_calcula_preco_prazo import \
    WebserviceCalculaPrecoPrazo
from pysigepweb.webservice_rastreamento import WebserviceRastreamento
from pysigepweb.tag_nacional import TagNacionalPAC41068
from pysigepweb.tag_plp import TagPLP
from pysigepweb.tag_remetente import TagRemetente
from pysigepweb.tag_dimensao_objeto import *
from pysigepweb.tag_objeto_postal import *
from pysigepweb.tag_correios_log import TagCorreiosLog
from pysigepweb.diretoria import Diretoria
from pysigepweb.endereco import Endereco
from pysigepweb.pysigep_exception import ErroConexaoComServidor
from pysigepweb.pysigep_exception import ErroTamanhoParamentroIncorreto
from pysigepweb.etiqueta import Etiqueta

LOGIN = 'sigep'
SENHA = 'n5f9t8'
CNPJ = '34028316000103'
CONTRATO = '9912208555'
CARTAO_POSTAGEM = '0057018901'


test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)


class TestWebserviceAtendeCliente(unittest.TestCase):

    def setUp(self):

        try:
            print u'[INFO] Iniciando Serviço de Atendimento ao  Cliente'
            self.sv = WebserviceAtendeCliente(WebserviceAtendeCliente.AMBIENTE_HOMOLOGACAO)
        except ErroConexaoComServidor as e:
            print e.message

    def test_consulta_status_cartao_postagem(self):

        print 'Cosultando dados do cliente'
        cliente = self.sv.busca_cliente(CONTRATO, CARTAO_POSTAGEM, LOGIN, SENHA)
        #
        #
        # print u'[INFO] Verificando status do cartão de postagem'
        # print sv.consulta_status_cartao_postagem(cartao_postagem.numero, cliente)


    def test_consulta_cep(self):
        print '[INFO] Consulta cep: %s' % '70002900'

        end_erp = self.sv.consulta_cep('70002900')

        print 'CEP:', end_erp.cep
        self.assertEqual(end_erp.cep, '70002900')

        print 'Bairro: ', end_erp.bairro
        self.assertEqual(end_erp.bairro, 'Asa Norte')

        print 'Cidade: ', end_erp.cidade
        self.assertEqual(end_erp.cidade, u'Brasília')

        print u'Endereço: ', end_erp.end
        self.assertEqual(end_erp.end, 'SBN Quadra 1 Bloco A')

        print 'UF:', end_erp.uf
        self.assertEqual(end_erp.uf, 'DF')

        # print 'Complemento: ', end_erp.complemento
        # self.assertRaises(ErroConexaoComServidor, end_erp.complemento, '')

        # print 'Id:', end_erp.id
        # self.assertRaises(ErroConexaoComServidor, end_erp.id, '')

        self.assertRaises(ErroTamanhoParamentroIncorreto, self.sv.consulta_cep,'0000000000')
        self.assertRaises(ErroConexaoComServidor, self.sv.consulta_cep,'00000000')

if __name__ == '__main__':
    unittest.main()
