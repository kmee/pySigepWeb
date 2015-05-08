# -*- coding: utf-8 -*-
from xml.etree.ElementTree import ElementTree, fromstring


class Destino(object):

    def __init__(self, root):
        self.local = root.find('local').text
        self.codigo = root.find('codigo').text
        self.cidade = root.find('cidade').text
        self.bairro = root.find('bairro').text
        self.uf = root.find('uf').text


class Evento(object):

    def __init__(self, root):
        self.tipo = root.find('tipo').text
        self.status = root.find('status').text
        self.data = root.find('data').text
        self.hora = root.find('hora').text
        self.descricao = root.find('descricao').text

        aux = root.find('recebedor')
        self.recebedor = aux.text if aux is not None else None

        aux = root.find('documento')
        self.documento = aux.text if aux is not None else None

        aux = root.find('comentario')
        self.comentario = aux.text if aux is not None else None

        self.local = root.find('local').text
        self.codigo = root.find('codigo').text
        self.cidade = root.find('cidade').text
        self.uf = root.find('uf').text
        self.sto = root.find('sto').text

        root_destino = root.find('destino')
        self.destino = Destino(root_destino) if root_destino is not None else\
            None


class Objeto(object):

    def __init__(self, root):
        self.numero = root.find('numero').text
        self.eventos = []

        for evento in root.findall('evento'):
            self.eventos.append(Evento(evento))


class RespostaRastreamento(object):

    def __init__(self, xml_retorno, etiquetas, backup_path=''):

        # tag raiz do xml
        root = fromstring(xml_retorno)

        try:
             # Cria backup do xml retornado
            ElementTree(root).write(backup_path + etiquetas + '.xml')
        except IOError as excp:
            print '[ERROR] ', excp.message

        self.versao = root.find('versao').text
        self.qtd = root.find('qtd').text
        self.tipo_pesquisa = root.find('TipoPesquisa').text
        self.tipo_resultado = root.find('TipoResultado').text
        self.objetos = {}

        for obj in root.findall('objeto'):
            aux = Objeto(obj)
            self.objetos[aux.numero] = aux
