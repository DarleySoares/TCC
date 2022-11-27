import os
import pandas as pd
import numpy as np
from pickle import dump
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


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

    
def get_clusters(X: list, data: pd.DataFrame):
    
    kmeans = KMeans(n_clusters=7)
    clusters = kmeans.fit_predict(X)
    dump(kmeans, open('kmeans.pkl', 'wb'))
    
    data["cluster"] = clusters
    
    return data

def clustered_properties(data: pd.DataFrame):
    
    columns =[
        "cd_grh", "tp_unidade", "vl_avaliacao_imovel", "perc_cota_financiamento", 
        "vl_financiamento", "vl_prestacao_maxima", "vl_encargo", "vl_area_privativa_util",
        "vl_area_comum", "vl_area_total", "vl_area_terreno", "vl_fracao_ideal_terreno", 
        "vl_percentual_ideal_terreno",  "tp_padrao_acabamento_imovel", 
        "nm_dormitorios_sem_banheiro", "nm_suites", "nm_total_dormitorios",
        "nm_vagas_garagem", "dc_empreendimento_y","ed_cep", "ed_tipo_logradouro", 
        "ed_logradouro", "ed_numero", "ed_bairro","ed_municipio", "ed_uf", 
        "nm_disponivel", "cluster"
    ]
    
    data = data[columns]
    
    if os.path.isfile(f'./data/analytics_data/consolidado/imoveis_clusterizados.csv'):
        data.to_csv(f'./data/analytics_data/consolidado/imoveis_clusterizados.csv', header=True, index=False)
    else:
        os.makedirs(f'./data/analytics_data/consolidado/', exist_ok=True) 
        data.to_csv(f'./data/analytics_data/consolidado/imoveis_clusterizados.csv', header=True, index=False)


def _processing_data(data: pd.DataFrame):
    
    columns = [
        "idade", "dc_sexo", "dc_estado_civil", "vl_renda_total",
        "fl_possui_outro_comprador_dependente", 
        "fl_conta_fgts_03_anos_com_requisitos", 
        "vl_prestacao_efetiva", "porc_prestacao_renda", 
        "vl_imovel", "faixa_pmcmv", "faixa_porc"
    ]
    
    string_columns = [
        "dc_sexo", "dc_estado_civil","ed_bairro", 
        "fl_possui_outro_comprador_dependente",
        "fl_conta_fgts_03_anos_com_requisitos"
    ]
    
    get_age = lambda x: (datetime.now() - datetime.strptime(x, "%d/%m/%Y")) // timedelta(days=365)
    data["idade"] = data["dt_nascimento_proponente"].apply(get_age)
    data["vl_imovel"] = data["vl_compra_venda"]/data["nm_total"]
    data["porc_prestacao_renda"] = np.round(100*(data["vl_prestacao_efetiva"]/data["vl_renda_total"]),2)
    data["faixa_pmcmv"] = data["vl_renda_total"].apply(salary_range)
    data["faixa_porc"] = data["porc_prestacao_renda"].apply(salary_percentage_range)

    for column in string_columns:
        data[column] = data[column].str.upper()
    
    data["dc_estado_civil"] = data["dc_estado_civil"].str.split(n=2).str[0]
    data["dc_estado_civil"] = data["dc_estado_civil"].str.replace("UNIÃO", "UNIÃO ESTÁVEL")
    data["dc_estado_civil"] = data["dc_estado_civil"].str.replace("SEPARADO", "DIVORCIADO")
    data["fl_possui_outro_comprador_dependente"] = data["fl_possui_outro_comprador_dependente"].fillna("NÃO")
    data.replace([np.inf, -np.inf], 100, inplace=True)
    
    output = data
    data = data[columns]
    
    data_dummie = pd.get_dummies(data)
    
    scaler = StandardScaler()
    X = scaler.fit_transform(data_dummie.values)
    dump(scaler, open('scaler.pkl', 'wb'))

    pca = PCA(n_components=2)
    X = pca.fit_transform(X)
    dump(pca, open('pca.pkl', 'wb'))
    
    output = get_clusters(X, output)
    clustered_properties(output)
    
    return X, output
