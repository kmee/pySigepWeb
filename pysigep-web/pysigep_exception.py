# -*- coding: utf-8 -*-


class SigepWEBBaseException(Exception):

    def __init__(self, msg, *args):
        self.message = msg.format(args)

    def __str__(self):
        return repr(self.message)


class ErroSemConecaoComInternet(SigepWEBBaseException):

    def __init__(self, msg, *args):
        self.message = u'Falha na conexão com a Internet'

    def __str__(self):
        return repr(self.message)


class ErroConexaoComServidor(SigepWEBBaseException):

    def __str__(self):
        return repr(self.message)


class ErroTamanhoParamentroIncorreto(SigepWEBBaseException):
    def __str__(self):
        return repr(self.message)


