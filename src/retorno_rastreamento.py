# -*- coding: utf-8 -*-


class Destino(object):

    def __init__(self, local, codigo, cidade, bairro, uf):
        self.local = local
        self.codigo = codigo
        self.cidade = cidade
        self.bairro = bairro
        self.uf = uf


class Evento(object):

    def __init__(self, tipo, status, data, descricao, local, codigo, cidade,
                 uf, sto):
        self.tipo = tipo
        self.status = status
        self.data = data
        self.descricao = descricao
        self.local = local
        self.codigo = codigo
        self.cidade = cidade
        self.uf = uf
        self.sto = sto


class Objeto(object):

    def __init__(self, numero):
        self.numero = numero
        self.eventos = []
        self.destino

    def add_evento(self, evento):
        self.eventos.append(evento)


class RetornoRastreamento(object):

    def __init__(self, xml_retorno):
        self.xml = xml_retorno
        self.qtd = 0
        self.tipo_pesquisa = ''
        self.tipo_resultado = ''
        self.objetos = []



#
# <sroxml>
#    <versao>1.0</versao>
#    <qtd>1</qtd>
#    <TipoPesquisa>Lista de Objetos</TipoPesquisa>
#    <TipoResultado>�ltimo evento</TipoResultado>
#      <objeto>
#        <numero>SS123456789BR</numero>
#        <evento>
#           <tipo>RO</tipo>
#           <status>01</status>
#           <data>09/02/2015</data>
#           <hora>17:32</hora>
#           <descricao>Objeto encaminhado</descricao>
#           <local>AC LUCAS DO RIO VERDE</local>
#           <codigo>78455970</codigo>
#           <cidade>Lucas Do Rio Verde</cidade>
#           <uf>MT</uf>
#           <sto>24300691</sto>
#        <destino>
#           <local>AC SINOP</local>
#           <codigo>78550970</codigo>
#           <cidade>Sinop</cidade>
#           <bairro>Centro</bairro>
#           <uf>MT</uf>
#        </destino>
#       </evento>
#      </objeto>
# </sroxml>
