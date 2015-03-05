# -*- coding: utf-8 -*-
from suds import client
import plp_xml_string

print 'Conectando...'

url = 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService' \
      '/AtendeCliente?wsdl'
# Instanciando um cliente
cliente = client.Client(url, cache=None)

# Listar os metodos que o webservice utiliza
# print cliente

sgpkey = {
    'usuario': 'sigep',
    'senha': 'n5f9t8',
    'cod_admin': '08082650',
    'contrato': '9912208555',
    'cartao': '0057018901',
    'numero_servico': '40215',
    'cep_origem': '70002900',
    'cep_destino': '74000100',
    'tipo_destinatario': 'C',
    'cnpj': '34028316000103',
    'quant_etiquetas': 1,
}

# Inicialização

# Verifica disponibilidade de servico
# verificaDisponibilidadeServico(codAdministrativo, numeroServico, cepOrigem, 
# cepDestino, usuario, senha)
# disponibilidade = cliente.service.verificaDisponibilidadeServico(
#     sgpkey['cod_admin'], sgpkey['numero_servico'],	sgpkey['cep_origem'],
#     sgpkey['cep_destino'], sgpkey['usuario'], sgpkey['senha'])

# Solicitar dados do contrato/cartao
# buscaCliente(string idContrato, string idCartaoPostagem, string usuario,
# string senha)
busca_cliente = cliente.service.buscaCliente(sgpkey['contrato'],
                                             sgpkey['cartao'],
                                             sgpkey['usuario'],
                                             sgpkey['senha'])
sgpkey['id_servico'] = long(104707)
cliente_cnpj = busca_cliente.cnpj
year = busca_cliente.dataAtualizacao.year
contrato_list = busca_cliente.contratos
cod_client = contrato_list[0].codigoCliente

print busca_cliente.contratos[0].contratoPK.numero
print busca_cliente.contratos[0].cartoesPostagem[0].codigoAdministrativo
print busca_cliente.contratos[0].cartoesPostagem[0].numero
print busca_cliente.nome


# Consulta CEP
# consultaCEP(string cep)
cep = cliente.service.consultaCEP(sgpkey['cep_origem'])
# bairro = cep.bairro

#print cep

# Verificando status do cartao
# getStatusCartaoPostagem(string numeroCartaoPostagem, string usuario,
# string senha)
# status = cliente.service.getStatusCartaoPostagem(sgpkey['cartao'],
#                                                  sgpkey['usuario'],
#                                                  sgpkey['senha'])

# Solicitar etiquetas por demanda
# solicitaEtiquetas(string tipoDestinatario, string identificador,
# long idServico, int qtdEtiquetas, string usuario, string senha)
range_etiquetas = cliente.service.solicitaEtiquetas(sgpkey['tipo_destinatario'],
                                                    sgpkey['cnpj'],
                                                    sgpkey['id_servico'],
                                                    sgpkey['quant_etiquetas'],
                                                    sgpkey['usuario'],
                                                    sgpkey['senha'])

print range_etiquetas
# etiq_inicial = range_etiquetas.split(',')[0].replace('S').replace(' BR')

etiqueta_inicial = range_etiquetas.split(',')[0]
# etiqueta_inicial = etiqueta_inicial.replace('SO', '')
etiqueta_number = int(etiqueta_inicial[2:10])
etiqueta_prefix = etiqueta_inicial[0:2]
etiqueta_sufix = etiqueta_inicial[10:]

etiquetas_sem_dig = []

for i in range(0, sgpkey['quant_etiquetas']):
    etiquetas_sem_dig.append(
        etiqueta_prefix + str(etiqueta_number + i).zfill(8) + etiqueta_sufix)

dig_verif_list = cliente.service.geraDigitoVerificadorEtiquetas(
    etiquetas_sem_dig, sgpkey['usuario'], sgpkey['senha'])

etiqueta_com_dig = []

# Adiciona digito verificador no espaco em branco da etiqueta
for i in range(0, sgpkey['quant_etiquetas']):
    aux = etiquetas_sem_dig[i].replace(' ', str(dig_verif_list[i]))
    etiqueta_com_dig.append(aux)

# print etiqueta_com_digito

xml = plp_xml_string.get_xml(busca_cliente, cep, etiqueta_com_dig)

print '[INFO] Validando xml'
if plp_xml_string.validate_XML(xml):
    print '[INFO] XML validado com sucesso!'
else:
    print '[ERROR] XML nao validou com sucesso!'

etq_sem_espaco = []

for etq in etiquetas_sem_dig:
    etq_sem_espaco.append(etq.replace(' ',''))

# fechaPlp(string xml, long idPlpCliente, string cartaoPostagem,
# string faixaEtiquetas, string usuario, string senha)
# fechaPlpVariosServicos(string xml, long idPlpCliente, string cartaoPostagem,
# string[] listaEtiquetas, string usuario, string senha)

# fechaPlp(string xml, long idPlpCliente, string cartaoPostagem, string
# faixaEtiquetas, string usuario, string senha)

# print cliente
plps = cliente.service.fechaPlpVariosServicos(
    xml, long(123), sgpkey['cartao'], etq_sem_espaco, sgpkey['usuario'],
    sgpkey['senha'])

# plps = cliente.service.fechaPlpVariosServicos(
#     xml, long(123), sgpkey['cartao'], etiquetas_sem_dig, sgpkey['usuario'],
#     sgpkey['senha'])

# Definindo url
url_calc = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?WSDL'

print '[INFO] Conectando webservice consulta prazo e preco'

# Instanciando um cliente
webservice_calc = client.Client(url_calc)

# print webservice_calc

# CalcPrecoPrazo(string nCdEmpresa, string sDsSenha, string nCdServico,
# string sCepOrigem, string sCepDestino, string nVlPeso, int nCdFormato,
# decimal nVlComprimento, decimal nVlAltura, decimal nVlLargura,
# decimal nVlDiametro, string sCdMaoPropria, decimal nVlValorDeclarado,
# string sCdAvisoRecebimento)

ret = webservice_calc.service.CalcPrecoPrazo(
    sgpkey['cod_admin'], sgpkey['senha'], sgpkey['numero_servico'],
    sgpkey['cep_origem'], sgpkey['cep_destino'], '1', 1, 100, 20, 20, 20,
    'S', 10, 'S')

# print ret

print 'Consulta finalizada'