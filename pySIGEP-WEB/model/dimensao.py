# -*- coding: utf-8 -*-


class TipoObjeto(object):

    _CODIGO = '000'

    def __init__(self, codigo):
        self._CODIGO = codigo
        self._altura = 0
        self._largura = 0
        self._comprimento = 0
        self._diametro = 0

    @property
    def codigo(self):
        return self._CODIGO

    @property
    def altura(self):
        return self._altura

    @property
    def largura(self):
        return self._largura

    @property
    def comprimento(self):
        return self._comprimento

    @property
    def diametro(self):
        return self._diametro


class Envelope(TipoObjeto):

    def __init__(self):
        super(TipoObjeto, self).__init__('001')


class Caixa(TipoObjeto):

    def __init__(self, altura, largura, comprimento):
        super(TipoObjeto, self).__init__('002')
        self._altura = altura
        self._largura = largura
        self._comprimento = comprimento


class Cilindro(TipoObjeto):

    def __init__(self, comprimento, diametro):
        super(TipoObjeto, self).__init__('003')
        self._comprimento = comprimento
        self._diametro = diametro


class Dimensao(object):

    def __init__(self, tipo_objeto):
        self.tipo_objeto = tipo_objeto

        if not isinstance(self.tipo_objeto, TipoObjeto):
            print 'tipo_objeto nao e instancia de TipoObjeto'

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
