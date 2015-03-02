
def get_xml():

    xml = '<?xml version=\"1.0\" encoding=\"ISO-8859-1\" ?>'
    xml += '<correioslog>'
    xml += '<tipo_arquivo>Postagem</tipo_arquivo>'
    xml += '<versao_arquivo>2.3</versao_arquivo>'
    xml += '<plp>' \
           '<id_plp/>' \
           '<valor_global/>'
    xml += '<mcu_unidade_postagem/><nome_unidade_postagem/>'
    xml += '<cartao_postagem>%s</cartao_postagem>'
    xml += 'EMPRESA BRASILEIRA DE CORREIOS E TELÉGRAFOS – ECT SIGEP Web - ' \
           'Manual de Implementação do Web Service 20/74</plp>'

    xml += '<remetente>'
    xml += '<numero_contrato>%s</numero_contrato>'
    xml += '<numero_diretoria>36</numero_diretoria>'
    xml += '<codigo_administrativo>%s</codigo_administrativo>'
    xml += '<nome_remetente><![CDATA[Empresa Ltda]]></nome_remetente>'
    xml += '<logradouro_remetente><![CDATA[Avenida Central]]> ' \
           '</logradouro_remetente>'

    xml += '<numero_remetente>2370</numero_remetente>'
    xml += '<complemento_remetente><![CDATA[sala 1205,12° andar]]> ' \
           '</complemento_remetente>'

    xml += '<bairro_remetente><![CDATA[Centro]]></bairro_remetente>'
    xml += '<cep_remetente><![CDATA[70002900]]></cep_remetente>'
    xml += '<cidade_remetente><![CDATA[Brasília]]></cidade_remetente>'
    xml += '<uf_remetente>PR</uf_remetente>'
    xml += '<telefone_remetente><![CDATA[6112345008]]></telefone_remetente>'
    xml += '<fax_remetente><![CDATA[]]></fax_remetente>'
    xml += '<email_remetente> <![CDATA[cli@mail.com.br]]> </email_remetente>'
    xml += '</remetente>' \
           '<forma_pagamento/>' \
           '<objeto_postal>'
    xml += '<numero_etiqueta>PH185560916BR</numero_etiqueta>'
    xml += '<codigo_objeto_cliente/>'
    xml += '<codigo_servico_postagem>41068</codigo_servico_postagem>'
    xml += '<cubagem>0,0000</cubagem>'
    xml += '<peso>200</peso>'
    xml += '<rt1/>' \
           '<rt2/>'
    xml += '<destinatario>'
    xml += '<nome_destinatario><![CDATA[Destino Ltda]]></nome_destinatario>'
    xml += '<telefone_destinatario><![CDATA[6212349644]]>' \
           '</telefone_destinatario>'

    xml += '<celular_destinatario><![CDATA[]]></celular_destinatario>'
    xml += '<email_destinatario><![CDATA[]]></email_destinatario>'
    xml += '<logradouro_destinatario><![CDATA[Avenida Central]]>' \
           '</logradouro_destinatario>'

    xml += '<complemento_destinatario><![CDATA[Qd: 102 A Lt: 04]]>' \
           '</complemento_destinatario>'

    xml += '<numero_end_destinatario>1065</numero_end_destinatario>'
    xml += '</destinatario>'

    xml += '<nacional>'
    xml += '<bairro_destinatario><![CDATA[Setor Industrial]]>' \
           '</bairro_destinatario>'
    xml += '<cidade_destinatario><![CDATA[Goiânia]]></cidade_destinatario>'
    xml += '<uf_destinatario>GO</uf_destinatario>'
    xml += '<cep_destinatario> <![CDATA[74000100]]></cep_destinatario>'
    xml += '<codigo_usuario_postal/>'
    xml += '<centro_custo_cliente/>'
    xml += '<numero_nota_fiscal>102030</numero_nota_fiscal>'
    xml += '<serie_nota_fiscal/>' \
           '<valor_nota_fiscal/>' \
           '<natureza_nota_fiscal/>'
    xml += '<descricao_objeto><![CDATA[]]></descricao_objeto>'
    xml += '<valor_a_cobrar>0,0</valor_a_cobrar>'
    xml += '</nacional>' \
           '<servico_adicional>'

    #O servico adicional 025 sempre deverá ser informado.
    xml += '<codigo_servico_adicional>025</codigo_servico_adicional>'
    xml += '<codigo_servico_adicional>001</codigo_servico_adicional>'
    xml += '<codigo_servico_adicional>019</codigo_servico_adicional>'
    xml += '<valor_declarado>99,00</valor_declarado>'
    xml += '</servico_adicional>'
    xml += '<dimensao_objeto>'
    xml += '<tipo_objeto>002</tipo_objeto>'
    xml += '<dimensao_altura>20</dimensao_altura>'
    xml += '<dimensao_largura>30</dimensao_largura>'
    xml += '<dimensao_comprimento>38</dimensao_comprimento>'
    xml += '<dimensao_diametro>0</dimensao_diametro>'
    xml += '</dimensao_objeto>'
    xml += '<data_postagem_sara/>'
    xml += '<status_processamento>0</status_processamento>'
    xml += '<numero_comprovante_postagem/>'
    xml += '<valor_cobrado/>'
    xml += '</objeto_postal>' \
           '</correioslog>'