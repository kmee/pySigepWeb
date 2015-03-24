# -*- coding: utf-8 -*-


class GeradorDigitoVerificador(object):

    @staticmethod
    def gera_digito_verificador(numero_etiqueta):

        multiplicadores = [8, 6, 4, 2, 3, 5, 9, 7]
        soma = 0

        if len(numero_etiqueta) != 8:
            numero_etiqueta = 'Erro'
        else:

            for i in range(8):
                soma += int(numero_etiqueta[i:(i+1)]) * multiplicadores[i]

            resto = soma % 11

            if resto == 0:
                dv = '5'
            elif resto == 1:
                dv = '0'
            else:
                dv = str(11 - resto)

            # numero_etiqueta += dv

        return dv
