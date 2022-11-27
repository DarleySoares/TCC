COLUMNS_CURATED = {
    'IDENTIFICAO DA PROPOSTA': ['N° da Proposta', 'N° do Contrato', 'Empreendimento', 'APF', 'Situação', 'Etapa', 'Produto', 'CNPJ do Construtor', 'Unidade Responsável', 'Razão Social', 'ID', 'Nome Arquivo'],
    'DADOS DA PRÉ-CONTRATAÇÃO': ['Pré-contratação', 'ID', 'Nome Arquivo'],
    'DADOS DA PROPOSTA': ['GRH', 'Unidade de Cobrança', 'Tipo de Financiamento', 'ID', 'Nome Arquivo'],
    'DADOS DO EMPREENDIMENTO GERAL': ['Descrição', 'Obra Concluída?', 'Data do Cadastro', 'Conceito de Risco', 'Data do Conceito de Risco', 'Percentual Mínimo de Obra Executada', 'Prazo Máximo de Latência', 'Percentual Mínimo de Unidades Comercializadas', 'Quantidade de Pavimentos', 'Situação Fundiária do Terreno', 'Modalidade', 'Indicador de prazo de latência', 'ID', 'Nome Arquivo'],
    'ENDEREÇO DO EMPREENDIMENTO': ['CEP', 'Tipo de Logradouro', 'Logradouro', 'Número', 'Bairro', 'Município', 'UF', 'ID', 'Nome Arquivo'],
    'GARANTIA': ['Tipo de Garantia', 'Código Garantia  SIRIC', 'Possui Penhor?', 'ID', 'Nome Arquivo'],
    'INFORMAÇÕES ADICIONAIS PARA EVOLUÇÃO': ['Regência Crítica', 'Regência de Evolução', 'Número Contrato', 'Sistema de Amortização', 'Situação na administração',' ', 'ID', 'Nome Arquivo'],
    'DADOS DO EMPREENDIMENTO': ['Nome', 'Agência', 'Quantidade Máxima de Unidades', 'Contrato APF', 'Município - UF', 'Número da Proposta', 'Valor do Empreendimento', 'Valor do Desconto', 'Data do Cadastro', 'Data do Trâmite', 'Fonte de Recurso', 'Situação do Empreendimento', 'ID', 'Nome Arquivo'],
    'TIPOS DE UNIDADES': ['TIPO DE IMÓVEL', 'TIPO', 'DISPONÍVEIS', 'VENDIDAS (FIN)', 'VENDIDAS (NÃO FIN)', 'PERMUTADAS', 'EM CONTRATAÇÃO', 'CONTRATADAS', 'ASSOCIADAS*', 'TOTAL', 'COMPRA/VENDA(R$)', 'AVALIAÇÃO(R$)', 'ID', 'Nome Arquivo'],
    'TIPO DA UNIDADE HABITACIONAL': ['Tipo de Unidade', 'Tipo de Imóvel', 'Categoria do Imóvel', 'Tipo de Construção', 'Área Privativa / Útil', 'Área Comum', 'Área Total', 'Área do Terreno', 'Fração Ideal do Terreno', 'Percentual Ideal do Terreno', 'Tipo de Implantação', 'Estado de Conservação do Condomínio', 'Testada', 'Estado de Conservação do Imóvel', 'Padrão de Acabamento do Imóvel', 'Descrição da Unidade', 'Descrição do Terreno', 'Dormitórios sem Banheiro', 'Suites', 'Total de Dormitórios', 'Vagas de Garagem', 'ID', 'Nome Arquivo'],
    'VALORES': ['Avaliação da Unidade', 'Orçamento/Compra e Venda da Unidade', 'ID', 'Nome Arquivo'],
    'QUANTIDADE DE UNIDADES': ['Disponíveis', 'Vendidas (Fin)', 'Vendidas (Não Fin)', 'Permutadas', 'Em Contratação', 'Contratadas', 'Associadas', 'Total', 'ID', 'Nome Arquivo'],
    'DADOS ADICIONAIS': ['ID', 'Nome Arquivo'],
}

RENAME_COLUMNS_CURATED = {
    'IDENTIFICAO DA PROPOSTA': ['nm_proposta', 'nm_contrato', 'dc_empreendimento', 'id_contrato_apf', 'dc_situacao', 'dc_etapa', 'cd_produto', 'nm_cnpj_construtor', 'cd_unidade_responsavel', 'dc_razao_social', 'id', 'nome_arquivo'],
    'DADOS DA PRÉ-CONTRATAÇÃO': ['id_pre_contratacao', 'id', 'nome_arquivo'],
    'DADOS DA PROPOSTA': ['cd_grh', 'cd_unidade_de_cobranca', 'tp_financiamento', 'id', 'nome_arquivo'],
    'DADOS DO EMPREENDIMENTO GERAL': ['dc_empreendimento', 'fl_obra_concluida', 'dt_cadastro', 'dc_conceito_risco', 'dt_conceito_risco', 'vl_percentual_min_obra_executada', 'vl_prazo_max_latencia', 'vl_percentual_min_unidades_comenrcializadas', 'nm_pavimentos', 'dc_situacao_fundiaria_terreno', 'tp_modalidade', 'dc_indicador_prazo_latencia', 'id', 'nome_arquivo'],
    'ENDEREÇO DO EMPREENDIMENTO': ['ed_cep', 'ed_tipo_logradouro', 'ed_logradouro', 'ed_numero', 'ed_bairro', 'ed_municipio', 'ed_uf', 'id', 'nome_arquivo'],
    'GARANTIA': ['tp_garantia', 'cd_garantia_siric', 'fl_penhor', 'id', 'nome_arquivo'],
    'INFORMAÇÕES ADICIONAIS PARA EVOLUÇÃO': ['cd_regencia_critica', 'dc_regencia_evolucao', 'nm_contrato', 'dc_sistema_de_amortizacao', 'dc_situacao_da_administracao',' ', 'id', 'nome_arquivo'],
    'DADOS DO EMPREENDIMENTO': ['dc_empreendimento', 'cd_agencia', 'nm_max_unidades', 'id_contrato_apf', 'dc_municipio_uf', 'nm_proposta', 'vl_empreendimento', 'vl_desconto', 'dt_cadastro', 'dt_tramite', 'dc_fonte_recurso', 'dc_situacao_empreendimento', 'id', 'nome_arquivo'],
    'TIPOS DE UNIDADES': ['tp_imovel', 'tp_unidade', 'nm_disponivel', 'nm_vendidas_finalizadas', 'nm_vendidas_nao_finalizadas', 'nm_permutadas', 'nm_em_contratacao', 'nm_contratadas', 'nm_associadas', 'nm_total', 'vl_compra_venda', 'vl_avaliacao', 'id', 'nome_arquivo'],
    'TIPO DA UNIDADE HABITACIONAL': ['tp_unidade', 'tp_imovel', 'dc_categoria_imovel', 'tp_construcao', 'vl_area_privativa_util', 'vl_area_comum', 'vl_area_total', 'vl_area_terreno', 'vl_fracao_ideal_terreno', 'vl_percentual_ideal_terreno', 'tp_implantacao', 'tp_estado_conservacao_condominio', 'vl_testada', 'tp_estado_conservacao_imovel', 'tp_padrao_acabamento_imovel', 'dc_unidade', 'dc_terreno', 'nm_dormitorios_sem_banheiro', 'nm_suites', 'nm_total_dormitorios', 'nm_vagas_garagem', 'id', 'nome_arquivo'],
    'VALORES': ['vl_avaliacao', 'evl_orcamento_compra_venda', 'id', 'nome_arquivo'],
    'QUANTIDADE DE UNIDADES': ['nm_disponiveis', 'nm_vendidas_finalizadas', 'nm_vendidas_nao_finalizadas', 'nm_permutadas', 'nm_em_construcao', 'nm_contratadas', 'nm_associadas', 'nm_total', 'id', 'nome_arquivo'],
    'DADOS ADICIONAIS': ['id', 'nome_arquivo'],
}  

area_columns = [
    "vl_area_privativa_util",
    "vl_area_comum",
    "vl_area_total",
    "vl_area_terreno",
    "vl_fracao_ideal_terreno",
]

categories_columns = [
    "tp_implantacao",
    "tp_estado_conservacao_condominio",
    "tp_estado_conservacao_imovel",
    "tp_padrao_acabamento_imovel",
]

float_columns = [
    "vl_percentual_ideal_terreno",
    "vl_testada",
    "vl_empreendimento",
    "vl_compra_venda",
    "vl_avaliacao",
]

COLUMNS_ANALYTICS = {
    "id":int,
    "tp_unidade": str,
    "cd_grh": str,
    "tp_imovel": str,
    "dc_categoria_imovel": str,
    "tp_construcao": str,
    "vl_area_privativa_util": float,
    "vl_area_comum": float,
    "vl_area_total": float,
    "vl_area_terreno": float,
    "vl_fracao_ideal_terreno": float,
    "vl_percentual_ideal_terreno": float,
    "tp_implantacao": str,
    "tp_estado_conservacao_condominio": str,
    "vl_testada": float,
    "tp_estado_conservacao_imovel": str,
    "tp_padrao_acabamento_imovel": str,
    "nm_dormitorios_sem_banheiro": int,
    "nm_suites": int,
    "nm_total_dormitorios": int,
    "nm_vagas_garagem": str,
    "dc_empreendimento": str,
    "id_contrato_apf":str,
    "dc_situacao": str,
    "dc_etapa": str,
    "nm_cnpj_construtor": str,
    "tp_financiamento": str,
    "vl_empreendimento": float,
    "dt_cadastro": str,
    "dt_tramite": str,
    "dc_situacao_empreendimento": str,
    "vl_percentual_min_obra_executada": str,
    "nm_pavimentos": int,
    "dc_situacao_fundiaria_terreno": str,
    "tp_modalidade": str,
    "dc_indicador_prazo_latencia": str,
    "ed_cep": str,
    "ed_tipo_logradouro": str,
    "ed_logradouro": str,
    "ed_numero": int,
    "ed_bairro": str,
    "ed_municipio": str,
    "ed_uf": str,
    "nm_disponivel": int,
    "nm_vendidas_finalizadas": int,
    "nm_vendidas_nao_finalizadas": int,
    "nm_permutadas": int,
    "nm_em_contratacao": int,
    "nm_contratadas": int,
    "nm_associadas": int,
    "nm_total": int,
    "vl_compra_venda":float,
    "vl_avaliacao": float,
}