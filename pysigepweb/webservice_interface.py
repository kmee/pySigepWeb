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

try:
    from suds import client
    from suds import WebFault
    from urllib2 import URLError
except ImportError as exp:
    print exp.message
    print 'Python module suds not installed. ' \
          'Please install with: sudo pip install suds'

from pysigep_exception import *


class WebserviceInterface(object):

    def __init__(self, url):
        self._url = url
        print '[INFO] Start SIGEPWEB webservice connection...'
        try:
            self._service = client.Client(url).service
        except client.TransportError as e:
            raise ErroConexaoComServidor(e.message)
