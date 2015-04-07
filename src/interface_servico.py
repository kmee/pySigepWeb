# -*- coding: utf-8 -*-
try:
    import suds
except ImportError as exp:
    print exp.message
    print u'Módulo suds não instalado. ' \
          u'Instale com: sudo pip install suds'
    exit(-1)


class InterfaceServico(object):

    def __init__(self, url):
        self._url = url
        print '[INFO] Conectando...'
        try:
            self._service = suds.client.Client(url).service
        except suds.client.TransportError as e:
            print "[ERRO] Erro em __init__. %s" % e.message
            exit(e.message)
