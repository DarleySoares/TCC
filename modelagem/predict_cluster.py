import pandas as pd
import numpy as np
from pickle import load


def salary_range(salary):
    if salary <= 1500:
        return "1"
    elif salary > 1500 and salary <= 2600:
        return "1.5"
    elif salary > 2600 and salary <= 4000:
        return "2"
    elif salary > 4000:
        return "3"


def salary_percentage_range(percentage):
    if percentage <= 25:
        return "0-25"
    elif percentage > 25 and percentage <= 50:
        return "25-50"
    elif percentage > 50:
        return "+50"

def _predict_cluster(data):
    
    columns = [
        "idade", "dc_sexo", "dc_estado_civil", "vl_renda_total",
        "fl_possui_outro_comprador_dependente", 
        "fl_conta_fgts_03_anos_com_requisitos", 
        "vl_prestacao_efetiva", "porc_prestacao_renda", 
        "vl_imovel", "faixa_pmcmv", "faixa_porc", "cluster"
    ]
    
    columns_dummie = [
        'idade', 'vl_renda_total', 'vl_prestacao_efetiva',
        'porc_prestacao_renda', 'vl_imovel', 'dc_sexo_FEMININO',
        'dc_sexo_MASCULINO', 'dc_estado_civil_CASADO(A)',
        'dc_estado_civil_DIVORCIADO(A)','dc_estado_civil_SOLTEIRO(A)', 
        'dc_estado_civil_UNIÃO ESTÁVEL','dc_estado_civil_VIÚVO(A)', 
        'fl_possui_outro_comprador_dependente_NÃO',
        'fl_possui_outro_comprador_dependente_SIM',
        'fl_conta_fgts_03_anos_com_requisitos_NÃO',
        'fl_conta_fgts_03_anos_com_requisitos_SIM', 'faixa_pmcmv_1',
        'faixa_pmcmv_1.5', 'faixa_pmcmv_2', 'faixa_pmcmv_3', 'faixa_porc_+50',
        'faixa_porc_0-25', 'faixa_porc_25-50'
    ]
    
    data = pd.DataFrame(data, index=[0])

    data["porc_prestacao_renda"] = np.round(100*(data["vl_prestacao_efetiva"]/data["vl_renda_total"]),2)
    data["faixa_pmcmv"] = data["vl_renda_total"].apply(salary_range)
    data["faixa_porc"] = data["porc_prestacao_renda"].apply(salary_percentage_range)
       
    sex_columns = ['dc_sexo_FEMININO','dc_sexo_MASCULINO']
    for col in sex_columns:
        data[col] = data['dc_sexo'] == col.split('_')[2]
        data[col] = data[col].astype(int)
        
    
    marital_status_columns = [
        'dc_estado_civil_CASADO(A)', 'dc_estado_civil_DIVORCIADO(A)', 
        'dc_estado_civil_SOLTEIRO(A)', 'dc_estado_civil_UNIÃO ESTÁVEL', 
        'dc_estado_civil_VIÚVO(A)'
    ]
    for col in marital_status_columns:
        data[col] = data['dc_estado_civil'] == col.split('_')[3]
        data[col] = data[col].astype(int)
    
    buyer_dependent_columns = [
        'fl_possui_outro_comprador_dependente_NÃO',
        'fl_possui_outro_comprador_dependente_SIM'
    ]
    for col in buyer_dependent_columns:
        data[col] = data['fl_possui_outro_comprador_dependente'] == col.split('_')[5]
        data[col] = data[col].astype(int)
    
    fgts_columns = [
        'fl_conta_fgts_03_anos_com_requisitos_NÃO',
        'fl_conta_fgts_03_anos_com_requisitos_SIM'
    ]
    for col in fgts_columns:
        data[col] = data['fl_conta_fgts_03_anos_com_requisitos'] == col.split('_')[7]
        data[col] = data[col].astype(int)
    
    range_pmcmv_columns = [
        'faixa_pmcmv_1', 'faixa_pmcmv_1.5',
        'faixa_pmcmv_2', 'faixa_pmcmv_3'
    ]
    for col in range_pmcmv_columns:
        data[col] = data['faixa_pmcmv'] == col.split('_')[2]
        data[col] = data[col].astype(int)
    
    range_percentage_columns = ['faixa_porc_+50', 'faixa_porc_0-25', 'faixa_porc_25-50']
    for col in range_percentage_columns:
        data[col] = data['faixa_porc'] == col.split('_')[2]
        data[col] = data[col].astype(int)
    
    data_dummie = data[columns_dummie]
    
    scaler = load(open('scaler.pkl', 'rb'))
    X = scaler.transform(data_dummie.values)
    
    pca = load(open('pca.pkl', 'rb'))
    X = pca.transform(X)
    
    kmeans = load(open('kmeans.pkl', 'rb'))
    cluster = kmeans.predict(X)
    data['cluster'] = cluster
    
    return X, data[columns]
  