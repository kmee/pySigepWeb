# -*- coding: utf-8 -*-
from suds import client


class InterfaceServico(object):

    def __init__(self, url):
        self.url = url

        print 'Conectando...'
        try:
            self.servico = client.Client(url).service
        except client.TransportError as exp:
            print exp.message
            exit(-1)
