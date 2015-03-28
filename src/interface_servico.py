# -*- coding: utf-8 -*-
from suds import client


class InterfaceServico(object):

    def __init__(self, url):
        self._url = url
        print 'Conectando...'
        try:
            self._service = client.Client(url).service
        except client.TransportError as exp:
            print self.__init__.__name__
            print exp.message
            exit(exp.message)
