PySIGEP Web - Correios
====================

Implementação SIGEP Web em Python permitindo integração com Web Service do 
Correios.

Recursos
---
Esta API pode:
* Calcular preços e prazos de entrega da encomenda.   
* TODO: Obter os dados de rastreamento das encomendas.   
* Verificar se um tipo de serviço (Sedex, PAC, ...) é permitido entre dois endereços.   
* Gerar e enviar o XML da pre-lista de postagem (PLP) para o Correios.   
* Gerar novos números de etiquetas de postagem.
* Criar e/ou verificar validade do dígito verificador das etiquetas (através do web service ou não).   
* TODO: Gerar o relatório da PLP no formato PDF.   
* TODO: Gerar as etiquetas de postagem no formato PDF.
* TODO: Gerar em PDF as chancelas para cada tipo de serviço (logo de cada tipo de servico). 

Requisitos
---

* python >= 2.7
* suds >= 0.4 

Instalação do suds: sudo pip install suds

Contribua
---

1. Faça um fork
2. Crie sua branch para a funcionalidade (`git checkout -b nova-funcionalidade`)
3. Faça o commit suas modificações (`git commit -am 'Adiciona nova funcionalidade'`)
4. Faça o push para a branch (`git push origin nova-funcionalidade`)
5. Crie um novo Pull Request
