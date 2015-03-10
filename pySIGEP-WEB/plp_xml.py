# -*- coding: utf-8 -*-


class PlpXML():

    def __init__(self):
        self.xml = ''

    def fill_xml(self, cliente, endereco, etiquetas):

        self.xml = u'<?self.xml version=\"1.0\" encoding=\"ISO-8859-1\"?>'
        self.xml += u'<correioslog>'
        self.xml += u'<tipo_arquivo>Postagem</tipo_arquivo>'
        self.xml += u'<versao_arquivo>2.3</versao_arquivo>'

        self.xml += u'<plp>'
        self.xml += u'<id_plp>123</id_plp>'
        self.xml += u'<valor_global></valor_global>'
        self.xml += u'<mcu_unidade_postagem></mcu_unidade_postagem>'
        self.xml += u'<nome_unidade_postagem></nome_unidade_postagem>'
        self.xml += u'<cartao_postagem>%s</cartao_postagem>' % \
                    cliente.contratos[0].cartoesPostagem[0].numero.zfill(10)
        self.xml += u'</plp>'

        self.xml += u'<remetente>'
        self.xml += u'<numero_contrato>%s</numero_contrato>' % \
                    cliente.contratos[0].contratoPK.numero.replace(' ', '')

        self.xml += u'<numero_diretoria>%d</numero_diretoria>' % \
                    int(cliente.contratos[0].codigoDiretoria)

        self.xml += u'<codigo_administrativo>%s</codigo_administrativo>' % \
                    cliente.contratos[0].cartoesPostagem[
                    0].codigoAdministrativo.replace(' ', '')

        self.xml += u'<nome_remetente><![CDATA[%s]]></nome_remetente>' % cliente.nome
        self.xml += u'<logradouro_remetente><![CDATA[Avenida Central]]> ' \
                    u'</logradouro_remetente>'

        self.xml += u'<numero_remetente>2370</numero_remetente>'
        self.xml += u'<complemento_remetente><![CDATA[%s]]> ' \
                    u'</complemento_remetente>' % endereco.complemento

        self.xml += u'<bairro_remetente><![CDATA[%s]]></bairro_remetente>' % \
               endereco.bairro
        self.xml += u'<cep_remetente><![CDATA[%s]]> </cep_remetente>' % \
                    endereco.cep
        self.xml += u'<cidade_remetente><![CDATA[%s]]></cidade_remetente>' % \
                    endereco.cidade
        self.xml += u'<uf_remetente>%s</uf_remetente>' % endereco.uf
        self.xml += u'<telefone_remetente><![CDATA[6112345008]]> ' \
                    u'</telefone_remetente>'
        self.xml += u'<fax_remetente><![CDATA[]]></fax_remetente>'
        self.xml += u'<email_remetente><![CDATA[cli@mail.com.br]]> ' \
                    u'</email_remetente>'
        self.xml += u'</remetente>'

        self.xml += u'<forma_pagamento></forma_pagamento>'

        self.xml += u'<objeto_postal>'

        self.xml += u'<numero_etiqueta>%s</numero_etiqueta>' % etiquetas[0]
        self.xml += u'<codigo_objeto_cliente></codigo_objeto_cliente>'
        self.xml += u'<codigo_servico_postagem>40215</codigo_servico_postagem>'
        self.xml += u'<cubagem></cubagem>'
        self.xml += u'<peso>200</peso>'
        self.xml += u'<rt1></rt1>'
        self.xml += u'<rt2></rt2>'

        self.xml += u'<destinatario>'
        self.xml += u'<nome_destinatario><![CDATA[Destino Ltda]]> ' \
                    u'</nome_destinatario>'
        self.xml += u'<telefone_destinatario><![CDATA[]]> ' \
                    u'</telefone_destinatario>'
        self.xml += u'<celular_destinatario><![CDATA[]]></celular_destinatario>'
        self.xml += u'<email_destinatario><![CDATA[]]></email_destinatario>'
        self.xml += u'<logradouro_destinatario><![CDATA[Avenida Central]]>' \
                    u'</logradouro_destinatario>'
        self.xml += u'<complemento_destinatario><![CDATA[Qd: 102 A Lt: 04]]>' \
                    u'</complemento_destinatario>'
        self.xml += u'<numero_end_destinatario>1065</numero_end_destinatario>'
        self.xml += u'</destinatario>'

        self.xml += u'<nacional>'
        self.xml += u'<bairro_destinatario><![CDATA[Setor Industrial]]>' \
                    u'</bairro_destinatario>'
        self.xml += u'<cidade_destinatario><![CDATA[Goiânia]]> ' \
                    u'</cidade_destinatario>'
        self.xml += u'<uf_destinatario>GO</uf_destinatario>'
        self.xml += u'<cep_destinatario><![CDATA[74000100]]></cep_destinatario>'
        self.xml += u'<codigo_usuario_postal></codigo_usuario_postal>'
        self.xml += u'<centro_custo_cliente></centro_custo_cliente>'
        self.xml += u'<numero_nota_fiscal>102030</numero_nota_fiscal>'
        self.xml += u'<serie_nota_fiscal>1</serie_nota_fiscal>'
        self.xml += u'<valor_nota_fiscal>99,0</valor_nota_fiscal>'
        self.xml += u'<natureza_nota_fiscal></natureza_nota_fiscal>'
        self.xml += u'<descricao_objeto><![CDATA[]]></descricao_objeto>'
        self.xml += u'<valor_a_cobrar>0,0</valor_a_cobrar>'
        self.xml += u'</nacional>'

        # O servico adicional 025 sempre deverá ser informado.
        self.xml += u'<servico_adicional>'
        self.xml += u'<codigo_servico_adicional>025</codigo_servico_adicional>'
        self.xml += u'<codigo_servico_adicional>001</codigo_servico_adicional>'
        self.xml += u'<codigo_servico_adicional>019</codigo_servico_adicional>'
        self.xml += u'<valor_declarado>99,00</valor_declarado>'
        self.xml += u'</servico_adicional>'

        self.xml += u'<dimensao_objeto>'
        self.xml += u'<tipo_objeto>002</tipo_objeto>'
        self.xml += u'<dimensao_altura>20</dimensao_altura>'
        self.xml += u'<dimensao_largura>30</dimensao_largura>'
        self.xml += u'<dimensao_comprimento>38</dimensao_comprimento>'
        self.xml += u'<dimensao_diametro>0</dimensao_diametro>'
        self.xml += u'</dimensao_objeto>'

        self.xml += u'<data_postagem_sara></data_postagem_sara>'
        self.xml += u'<status_processamento>0</status_processamento>'
        self.xml += u'<numero_comprovante_postagem> ' \
                    u'</numero_comprovante_postagem>'
        self.xml += u'<valor_cobrado></valor_cobrado>'
        self.xml += u'</objeto_postal>'
        self.xml += u'</correioslog>'

        return self.xml
