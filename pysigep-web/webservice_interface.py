# -*- coding: utf-8 -*-
try:
    from suds import client
    from suds import WebFault
    from urllib2 import URLError
except ImportError as exp:
    print exp.message
    print u'Módulo suds não instalado. ' \
          u'Instale com: sudo pip install suds'
    exit(-1)

# import logging
# logging.basicConfig(level=logging.DEBUG)
from pysigep_exception import *


class WebserviceInterface(object):

    def __init__(self, url):
        self._url = url
        print '[INFO] Conectando...'
        try:
            self._service = client.Client(url).service
        except client.TransportError as e:
            # print "[ERRO] Erro em __init__. %s" % e.message
            # exit(e.message)
            raise ErroConexaoComServidor(e.message)
