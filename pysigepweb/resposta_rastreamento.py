# -*- coding: utf-8 -*-
# #############################################################################
#
#    Brazillian Carrier Correios Sigep WEB
#    Copyright (C) 2015 KMEE (http://www.kmee.com.br)
#    @author: Michell Stuttgart <michell.stuttgart@kmee.com.br>
#
#    Sponsored by Europestar www.europestar.com.br
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

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

        self.error = ''
        self.versao = root.find('versao').text
        self.qtd = 0
        self.tipo_pesquisa = ''
        self.tipo_resultado = ''
        self.objetos = {}

        self._parse(root)

    def _parse(self, root):

        self.error = root.find('error')

        if self.error == '0':
            self.qtd = root.find('qtd').text
            self.tipo_pesquisa = root.find('TipoPesquisa').text
            self.tipo_resultado = root.find('TipoResultado').text

            for obj in root.findall('objeto'):
                aux = Objeto(obj)
                self.objetos[aux.numero] = aux
