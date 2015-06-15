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

#
# class TipoObjeto(object):
#
#     def __init__(self, codigo):
#         self._codigo = codigo
#
#     @property
#     def codigo(self):
#         return self._codigo
#
#
# class Envelope(TipoObjeto):
#
#     def __init__(self, altura=2, largura=11, comprimento=16):
#         super(Envelope, self).__init__('001')
#         self.altura = altura
#         self.largura = largura
#         self.comprimento = comprimento
#
#
# class Caixa(TipoObjeto):
#
#     def __init__(self, altura=2, largura=11, comprimento=16):
#         super(Caixa, self).__init__('002')
#
#         # if altura not in xrange(2, 105):
#         #     print u'[AVISO] Altura da Caixa deve ser igual ou maior que 2.'
#         #
#         # if largura not in xrange(11, 105):
#         #     print u'[AVISO] Largura da Caixa deve ser igual ou maior que 11.'
#         #
#         # if comprimento not in xrange(16, 105):
#         #     print u'[AVISO] Comprimento da Caixa deve ser igual ou maior ' \
#         #           u'que 16.'
#
#         self.altura = altura
#         self.largura = largura
#         self.comprimento = comprimento
#
#
# class Pacote(TipoObjeto):
#     def __init__(self, altura=2, largura=11, comprimento=16):
#         super(Pacote, self).__init__('002')
#
#         # if altura not in xrange(2, 105):
#         #     print u'[AVISO] Altura da Pacote deve ser igual ou maior que 2.'
#         #
#         # if largura not in xrange(11, 105):
#         #     print u'[AVISO] Largura da Pacote deve ser igual ou maior que 11.'
#         #
#         # if comprimento not in xrange(16, 105):
#         #     print u'[AVISO] Comprimento da Pacote deve ser igual ou maior ' \
#         #           u'que 16.'
#
#         self.altura = altura
#         self.largura = largura
#         self.comprimento = comprimento
#
#
# class Cilindro(TipoObjeto):
#
#     def __init__(self, comprimento=18, diametro=5):
#         super(Cilindro, self).__init__('003')
#
#         # if comprimento not in xrange(18, 105):
#         #     print u'[AVISO] Comprimento da Cilindro deve ser igual ou maior ' \
#         #           u'que 18.'
#         #
#         # if diametro not in xrange(5, 105):
#         #     print u'[AVISO] Diametro da Cilindro deve ser igual ou maior que 5.'
#
#         self.comprimento = comprimento
#         self.diametro = diametro
#
#
# class Rolo(TipoObjeto):
#
#     def __init__(self, comprimento=18, diametro=5):
#         super(Rolo, self).__init__('003')
#
#         # if comprimento not in xrange(18, 105):
#         #     print u'[AVISO] Comprimento da Rolo deve ser igual ou maior que 18.'
#         #
#         # if diametro not in xrange(5, 105):
#         #     print u'[AVISO] Diametro da Rolo deve ser igual ou maior que 5.'
#
#         self.comprimento = comprimento
#         self.diametro = diametro


class Dimensao(object):

    TIPO_ENVELOPE = '001'
    TIPO_CAIXA = '002'
    TIPO_CILINDRO = '003'

    def __init__(self, codigo, altura=2, largura=11, comprimento=16,
                 diametro=5):
        self.codigo = codigo
        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento
        self.diametro = diametro

