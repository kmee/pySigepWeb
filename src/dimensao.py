# -*- coding: utf-8 -*-


class TipoObjeto(object):

    _CODIGO = '000'

    def __init__(self, codigo):
        self._CODIGO = codigo
        self.altura = 0
        self.largura = 0
        self.comprimento = 0
        self.diametro = 0

    @property
    def codigo(self):
        return self._CODIGO


class Envelope(TipoObjeto):

    def __init__(self):
        super(Envelope, self).__init__('001')


class Caixa(TipoObjeto):

    def __init__(self, altura, largura, comprimento):
        super(Caixa, self).__init__('002')
        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento


class Pacote(Caixa):
    def __init__(self, altura, largura, comprimento):
        super(Pacote, self).__init__(altura, largura, comprimento)


class Cilindro(TipoObjeto):

    def __init__(self, comprimento, diametro):
        super(Cilindro, self).__init__('003')
        self.comprimento = comprimento
        self.diametro = diametro


class Rolo(Cilindro):

    def __init__(self, comprimento, diametro):
        super(Rolo, self).__init__(comprimento, diametro)


class Dimensao(object):

    def __init__(self, tipo_objeto):
        self.tipo_objeto = tipo_objeto

        if not isinstance(self.tipo_objeto, TipoObjeto):
            raise TypeError(str(tipo_objeto) + u' não é instancia de '
                                               u'TipoObjeto')

    @property
    def codigo(self):
        return self.tipo_objeto.codigo

    @property
    def altura(self):
        return self.tipo_objeto.altura

    @property
    def largura(self):
        return self.tipo_objeto.largura

    @property
    def comprimento(self):
        return self.tipo_objeto.comprimento

    @property
    def diametro(self):
        return self.tipo_objeto.diametro
