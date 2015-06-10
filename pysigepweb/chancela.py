# -*- coding: utf-8 -*-
# #############################################################################
#
#    Brazillian Carrier Correios Sigep WEB
#    Copyright (C) 2015 KMEE (http://www.kmee.com.br)
#    @author: Michell Stuttgart <michell.stuttgart@kmee.com.br>
#    @author: Rodolfo Bertozo <rodolfo.bertozo@kmee.com.br>
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
from PIL import Image, ImageDraw, ImageFont
from StringIO import StringIO
import io
import base64
import os

BASE_DIR = os.path.dirname(__file__)


class Chancela(object):

    _TTF_ARIAL = os.path.join(BASE_DIR, 'data/fonts/arial.ttf')
    _TTF_ARIAL_N = os.path.join(BASE_DIR, 'data/fonts/arial_negrito.ttf')

    def __init__(self, base_64_str_imagem, descricao, num_contrato='000000000',
                 ano_assinatura='0000', dr_origem='XX', dr_postagem='YY',
                 nome_cliente='cliente'):

        self._base_64_str_imagem = str(base_64_str_imagem)
        self.descricao = str(descricao)
        self.num_contrato = num_contrato
        self.ano_assinatura = ano_assinatura
        self.dr_origem = dr_origem
        self.dr_postagem = dr_postagem
        self.nome_cliente = nome_cliente

    @property
    def base_64_str_imagem(self):
        return self._base_64_str_imagem

    def get_image_base64(self):

        if self.dr_origem != self.dr_postagem:
            texto = "%s/%s - DR/%s/%s" % (self.num_contrato,
                                          self.ano_assinatura,
                                          self.dr_origem,
                                          self.dr_postagem)
        else:
            texto = "%s/%s - DR/%s" % (self.num_contrato,
                                       self.ano_assinatura,
                                       self.dr_origem)

        t = base64.decodestring(self._base_64_str_imagem)
        imagem = Image.open(StringIO(t))
        img = imagem.convert("RGB")
        draw = ImageDraw.ImageDraw(img)

        font = ImageFont.truetype(Chancela._TTF_ARIAL, 8)
        draw.setfont(font)
        tamanho_texto = draw.textsize(texto)
        h_position = (img.size[0] - tamanho_texto[0]) / 2
        v_position = img.size[1] / 2
        draw.text((h_position, v_position), texto, fill=(0, 0, 0))

        font = ImageFont.truetype(Chancela._TTF_ARIAL_N, 11)
        draw.setfont(font)
        tamanho_texto = draw.textsize(self.nome_cliente)
        h_position = (img.size[0] - tamanho_texto[0]) / 2
        v_position = img.size[1] / 2 + 8
        draw.text((h_position, v_position), self.nome_cliente, fill=(0, 0, 0))

        # Converte a imagem resultante para base64
        tmp = io.BytesIO()
        img.save(tmp, 'png')
        img = base64.b64encode(tmp.getvalue())

        return img

    def save_image(self, path):
        with open(path + 'jpg', 'wb') as f:
            f.write(base64.decodestring(self._base_64_str_imagem))

