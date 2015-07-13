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
import textwrap

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

    @property
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

        # A imagem fornecida pelo metodo busca_cliente retorna a imagem em
        # base64
        t = base64.decodestring(self._base_64_str_imagem)
        img = Image.open(StringIO(t)).convert("RGB")
        draw = ImageDraw.ImageDraw(img)

        # Inicializamos a fonte a ser usada no nome da empresa presente na
        # chancela
        font = ImageFont.truetype(Chancela._TTF_ARIAL, int(img.size[0]*0.07))
        draw.setfont(font)
        tamanho_texto = draw.textsize(texto)
        h_position = (img.size[0] - tamanho_texto[0]) / 2
        v_position = img.size[1] / 2
        draw.text((h_position, v_position), texto, fill=(0, 0, 0))

        # Dividimos o nome da empresa em partes para que seja possivel usar
        # quebra de linha
        list_name = textwrap.wrap(self.nome_cliente, width=20)

        font = ImageFont.truetype(Chancela._TTF_ARIAL_N, int(img.size[0]*0.07))
        draw.setfont(font)
        v_position = img.size[1] / 2 + int(img.size[0]*0.07)

        y_text = v_position
        for line in list_name:
            width, height = font.getsize(line)
            h_position = (img.size[0] - width) / 2
            draw.text((h_position, y_text), line, fill=(0, 0, 0))
            y_text += height + 5

        size = max(img.size[0], img.size[1])
        bg = Image.new("RGBA", (size, size), (255, 255, 255))
        h_position = (bg.size[0] - img.size[0]) / 2
        v_position = (bg.size[1] - img.size[1]) / 2

        bg.paste(img, box=(h_position, v_position))

        # Converte a imagem resultante para base64
        tmp = io.BytesIO()
        bg.save(tmp, 'png')
        bg = base64.b64encode(tmp.getvalue())

        return bg

    def save_image(self, path):
        with open(path + 'jpg', 'wb') as f:
            f.write(base64.decodestring(self._base_64_str_imagem))
