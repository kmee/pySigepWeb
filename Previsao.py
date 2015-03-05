# -*- coding: utf-8 -*-
# Importacoes
import urllib2
from xml.dom import minidom


class Previsao():
    # URL do INMET - WebService
    url = 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService' \
          '/AtendeCliente?wsdl'
    fonte = ''
    xmlDoc = ''
    listaEstado = []

    def __init__(self):
        try:
            self.fonte = urllib2.urlopen(self.url).read()
        except:
            self.fonte = 'URL Inválida'
        self.xmlDoc = minidom.parseString(self.fonte)

    def getTag(self, tag):
        self.listaEstado = self.xmlDoc.getElementsByTagName(tag)

    def listElement(self):
        for x in self.listaEstado:
            print x.toxml()

objPrevisao = Previsao()
listaEstado = objPrevisao.getTag('estado')
objPrevisao.listElement()
