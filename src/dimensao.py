# -*- coding: utf-8 -*-


class TipoObjeto(object):

    def __init__(self, codigo):
        self._codigo = codigo
        self.altura = 0
        self.largura = 0
        self.comprimento = 0
        self.diametro = 0

    @property
    def codigo(self):
        return self._codigo


class Envelope(TipoObjeto):

    def __init__(self):
        super(Envelope, self).__init__('001')
        self.altura = 2
        self.largura = 11
        self.comprimento = 16
        self.diametro = 5


class Caixa(TipoObjeto):

    def __init__(self, altura=2, largura=11, comprimento=16):
        super(Caixa, self).__init__('002')

        if altura not in xrange(2, 105):
            print 'u[AVISO] Altura da Caixa deve ser igual ou maior que 2.'
            print 'u[AVISO] Altura da Caixa recebe valor mínimo igual a 2.'
            altura = 2

        if largura not in xrange(11, 105):
            print 'u[AVISO] Largura da Caixa deve ser igual ou maior que 11.'
            print 'u[AVISO] Largura da Caixa recebe valor mínimo igual a 11.'
            largura = 11

        if comprimento not in xrange(16, 105):
            print 'u[AVISO] Comprimento da Caixa deve ser igual ou maior ' \
                  'que 16.'
            print 'u[AVISO] comprimento da Caixa recebe valor mínimo igual a' \
                  ' 16.'
            comprimento = 16

        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento


class Pacote(TipoObjeto):
    def __init__(self, altura=2, largura=11, comprimento=16):
        super(Pacote, self).__init__('002')

        if altura not in xrange(2, 105):
            print 'u[AVISO] Altura da Pacote deve ser igual ou maior que 2.'
            print 'u[AVISO] Altura da Pacote recebe valor mínimo igual a 2.'
            altura = 2

        if largura not in xrange(11, 105):
            print 'u[AVISO] Largura da Pacote deve ser igual ou maior que 11.'
            print 'u[AVISO] Largura da Pacote recebe valor mínimo igual a 11.'
            largura = 11

        if comprimento not in xrange(16, 105):
            print 'u[AVISO] Comprimento da Pacote deve ser igual ou maior ' \
                  'que 16.'
            print 'u[AVISO] comprimento da Pacote recebe valor mínimo igual a' \
                  ' 16.'
            comprimento = 16

        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento


class Cilindro(TipoObjeto):

    def __init__(self, comprimento=18, diametro=5):
        super(Cilindro, self).__init__('003')

        if comprimento not in xrange(18, 105):
            print 'u[AVISO] Comprimento da Cilindro deve ser igual ou maior ' \
                  'que 18.'
            print 'u[AVISO] Comprimento da Cilindro recebe valor mínimo igual' \
                  ' a 18.'
            comprimento = 18

        if diametro not in xrange(5, 105):
            print 'u[AVISO] Diametro da Cilindro deve ser igual ou maior ' \
                  'que 5.'
            print 'u[AVISO] Diametro da Cilindro recebe valor mínimo igual' \
                  ' a 5.'
            diametro = 5

        self.comprimento = comprimento
        self.diametro = diametro


class Rolo(TipoObjeto):

    def __init__(self, comprimento=18, diametro=5):
        super(Rolo, self).__init__('003')

        if comprimento not in xrange(18, 105):
            print 'u[AVISO] Comprimento da Rolo deve ser igual ou maior ' \
                  'que 18.'
            print 'u[AVISO] Comprimento da Rolo recebe valor mínimo igual' \
                  ' a 18.'
            comprimento = 18

        if diametro not in xrange(5, 105):
            print 'u[AVISO] Diametro da Rolo deve ser igual ou maior ' \
                  'que 5.'
            print 'u[AVISO] Diametro da Rolo recebe valor mínimo igual' \
                  ' a 5.'
            diametro = 5

        self.comprimento = comprimento
        self.diametro = diametro


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
