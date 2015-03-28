# -*- coding: utf-8 -*-
from src import plp_xml_validator
from src.tag_destinatario import TagDestinatario
from src.tag_nacional import TagNacional
from src.tag_dimensao_objeto import TagDimensaoObjeto
from src.etiqueta import Etiqueta
from src.servico_postagem import ServicoPostagem
from src.tag_servico_adicional import TagServicoAdicional
from src.tag_base import TagBase


class TagObjetoPostal(TagBase):

    def __init__(self, obj_destinatario, obj_nacional, obj_dimensao_objeto,
                 obj_servico_postagem, obj_servico_adicional, ob_etiqueta, peso,
                 status_processamento, codigo_objeto_cliente='',
                 cubagem=0.0000, numero_comprovante_de_postagem=0,
                 valor_cobrado=0.0, rt1='', rt2=''):

        if not isinstance(obj_destinatario, TagDestinatario):
            raise TypeError
        self.destinatario = obj_destinatario

        if not isinstance(obj_nacional, TagNacional):
            raise TypeError
        self.nacional = obj_nacional

        if not isinstance(obj_dimensao_objeto, TagDimensaoObjeto):
            raise TypeError
        self.dimensao_objeto = obj_dimensao_objeto

        if not isinstance(obj_servico_postagem, ServicoPostagem):
            raise TypeError
        self.servico_postagem = obj_servico_postagem

        if not isinstance(obj_servico_adicional, TagServicoAdicional):
            raise TypeError
        self.servico_adicional = obj_servico_adicional

        if not isinstance(ob_etiqueta, Etiqueta):
            raise TypeError
        self.etiqueta = ob_etiqueta

        self.codigo_objeto_cliente = codigo_objeto_cliente
        self.cubagem = cubagem
        self.peso = peso
        # self.data_postagem = date()
        self.status_processamento = status_processamento
        self.numero_comprovante_de_postagem = numero_comprovante_de_postagem
        self.valor_cobrado = valor_cobrado
        self.rt1 = rt1
        self.rt2 = rt2

    def get_xml(self):

        xml = u'<objeto_postal>'
        xml += u'<numero_etiqueta>%s</numero_etiqueta>' % \
               self.etiqueta.etiqueta_com_dig_verif
        xml += u'<codigo_objeto_cliente>%s</codigo_objeto_cliente>' % \
               self.codigo_objeto_cliente
        xml += u'<codigo_servico_postagem>%s</codigo_servico_postagem>' % \
               self.servico_postagem.codigo

        aux = str(self.cubagem) if self.cubagem else ''
        xml += u'<cubagem>%s</cubagem>' % aux

        xml += u'<peso>%d</peso>' % self.peso
        xml += u'<rt1>%s</rt1>' % self.rt1
        xml += u'<rt2>%s</rt2>' % self.rt2
        xml += self.destinatario.get_xml()
        xml += self.nacional.get_xml()
        xml += self.servico_adicional.get_xml()
        xml += self.dimensao_objeto.get_xml()
        xml += u'<data_postagem_sara></data_postagem_sara>'
        xml += u'<status_processamento>%s</status_processamento>' % \
               self.status_processamento

        aux = str(self.numero_comprovante_de_postagem) if \
            self.numero_comprovante_de_postagem else ''
        xml += u'<numero_comprovante_postagem>%s</numero_comprovante_postagem' \
               u'>' % aux

        aux = str(self.valor_cobrado) if self.valor_cobrado else ''
        xml += u'<valor_cobrado>%s</valor_cobrado>' % aux

        xml += u'</objeto_postal>'

        TagObjetoPostal.validar_xml(xml)
        return xml

    @staticmethod
    def validar_xml(xml):

        if plp_xml_validator.validate_xml(xml):
            print u'XML TagObjetoPostal validado com sucesso!'
        else:
            print u'Validação de XML TagObjetoPostal falhou!'

