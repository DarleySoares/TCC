import pandas as pd

def get_properties(input, cluster):
    
    properties_columns = [
        'dc_empreendimento_y',
        'ed_endereco',
        'vl_area_privativa_util', 
        'nm_dormitorios_sem_banheiro',
        'nm_suites',
        'nm_total_dormitorios',
        'nm_vagas_garagem',
        'vl_avaliacao_imovel', 
        'score'
    ]

    properties_integer_columns = [
        'r_vlimov',
        'r_vlfin',
        'r_prest',
        'r_area',
        'r_dorm',
        'r_sui',
        'r_gar',
        'r_porvl'
    ]

    properties = pd.read_csv('./data/analytics_data/consolidado/imoveis_clusterizados.csv')
    
    properties['r_vlimov'] = properties['vl_avaliacao_imovel'] <= input['vl_imovel']
    properties['r_porvl'] = (properties['vl_avaliacao_imovel'] / input['vl_imovel']) <= 1
    properties['r_vlfin'] = (properties['vl_avaliacao_imovel'] - input['vl_entrada']) <= properties['vl_financiamento']
    properties['r_prest'] = properties['vl_prestacao_maxima'] <= input['vl_prestacao_efetiva'] 
    properties['r_area'] = properties['vl_area_privativa_util'] >= input['area_min'] 
    properties['r_dorm'] = properties['nm_total_dormitorios'] >= input['nm_total_dormitorios'] 
    properties['r_sui'] = properties['nm_suites'] >= input['nm_suites'] 
    properties['r_gar'] = properties['nm_vagas_garagem'] >= input['nm_vagas_garagem']
    
    properties = properties[properties["cluster"] == cluster]
    properties = properties.drop_duplicates(subset=["cd_grh", "tp_unidade", "vl_avaliacao_imovel"])
    
    for col in properties_integer_columns:
        properties[col] = properties[col].astype(int)
        
    peso1 = ['r_area', 'r_dorm', 'r_sui', 'r_gar']
    peso1_5 = ['r_vlfin', 'r_prest']
    peso2 = ['r_vlimov', 'r_porvl']

    properties["score"] = 10*(0.75*properties[peso1].sum(axis = 1) + 1.5*properties[peso1_5].sum(axis = 1) + 2*properties[peso2].sum(axis = 1))
    properties["ed_endereco"] = properties['ed_tipo_logradouro'].str.upper() + ' ' + properties['ed_logradouro'].str.upper() + ', ' + properties['ed_numero'].astype(int).round(0).astype(str) + ', ' + properties['ed_bairro'].str.upper()
    properties["dc_empreendimento_y"] = properties["dc_empreendimento_y"].str.upper()
    
    output = properties[properties_columns+properties_integer_columns].sort_values(by=["score"], ascending = False)
    output.columns = ["Empreendimento", "Endereço", "Área Total",
        "Nº de quartos sem suíte", "Nº de suítes", 
        "Nº de quartos", "Nº de vagas de garagem",
        "Valor do imóvel", "Score",  "r_vlimov", 
        "r_vlfin", "r_prest", "r_area", 
        "r_dorm", "r_sui", "r_gar", "r_porvl"
    ]
    return output