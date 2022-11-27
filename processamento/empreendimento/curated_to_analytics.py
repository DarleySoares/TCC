import os
import pandas as pd
pd.options.mode.chained_assignment = None

from utils.constants_empreendimento import COLUMNS_ANALYTICS, area_columns, categories_columns, float_columns
from utils.functions import format_area, format_categories, format_coin, format_float, format_garagem, format_percentage


def _preprocessing_curated_to_analytics_empreendimento() -> None:

    tipo_da_unidade_habitacional = pd.read_csv('./data/curated_data/empreendimento/TIPO DA UNIDADE HABITACIONAL/TIPO DA UNIDADE HABITACIONAL.csv')

    identificacao_da_proposta = pd.read_csv('./data/curated_data/empreendimento/IDENTIFICAO DA PROPOSTA/IDENTIFICAO DA PROPOSTA.csv')
    dados_da_proposta = pd.read_csv(f'./data/curated_data/empreendimento/DADOS DA PROPOSTA/DADOS DA PROPOSTA.csv')
    dados_do_empreendimento_geral = pd.read_csv(f'./data/curated_data/empreendimento/DADOS DO EMPREENDIMENTO GERAL/DADOS DO EMPREENDIMENTO GERAL.csv')
    dados_do_empreendimento = pd.read_csv(f'./data/curated_data/empreendimento/DADOS DO EMPREENDIMENTO/DADOS DO EMPREENDIMENTO.csv')
    endereco_do_empreendimento = pd.read_csv(f'./data/curated_data/empreendimento/ENDEREÇO DO EMPREENDIMENTO/ENDEREÇO DO EMPREENDIMENTO.csv')
    tipo_de_unidades = pd.read_csv(f'./data/curated_data/empreendimento/TIPOS DE UNIDADES/TIPOS DE UNIDADES.csv')

    dimension_tables = [
        (identificacao_da_proposta, "id"), 
        (dados_da_proposta, "id"),
        (dados_do_empreendimento_geral, "id"),
        (dados_do_empreendimento, "id"),
        (endereco_do_empreendimento, "id"),
        (tipo_de_unidades, ["id", "tp_unidade"]),
    ]


    for df, i in zip(dimension_tables, range(0, len(dimension_tables))):
        if i == 0:
            analytics = pd.merge(tipo_da_unidade_habitacional, df[0], how = "left", on = df[1])
        else:
            analytics = pd.merge(analytics, df[0], how = "left", on = df[1])
            
    analytics.drop(columns= ["nome_arquivo_x", "nome_arquivo_y", "tp_imovel_y", "nm_proposta_y", "id_contrato_apf_y", "dt_cadastro_y"], inplace= True)
    analytics.rename(columns = {"tp_imovel_x": "tp_imovel"}, inplace= True)
    analytics.rename(columns = {"nm_proposta_x": "nm_proposta"}, inplace= True)
    analytics.rename(columns = {"id_contrato_apf_x": "id_contrato_apf"}, inplace= True)
    analytics.rename(columns = {"dt_cadastro_x": "dt_cadastro"}, inplace= True)
    
    output = analytics[COLUMNS_ANALYTICS.keys()]
    
    for column in area_columns:
        output[column] = output.apply(lambda df: format_area(df[column]), axis = 1)
        
    for column in categories_columns:
        output[column] = output.apply(lambda df: format_categories(df[column]), axis = 1)

    for column in float_columns:
        output[column] = output.apply(lambda df: format_float(df[column]), axis = 1)
        
    output["nm_vagas_garagem"] = output.apply(lambda df: format_garagem(df["nm_vagas_garagem"]), axis = 1)
    output["vl_percentual_ideal_terreno"] = output.apply(lambda df: format_percentage(df["vl_percentual_ideal_terreno"]), axis = 1)
    output["vl_empreendimento"] = output.apply(lambda df: format_coin(df["vl_empreendimento"]), axis = 1)
    output["nm_associadas"] = output["nm_associadas"].fillna(0)
    output["nm_pavimentos"] = output["nm_pavimentos"].fillna(0)

    for column, typ in COLUMNS_ANALYTICS.items():
        output[column] = output[column].astype(typ)
    
    if os.path.isfile(f'./data/analytics_data/empreendimento/analytics.csv'):
        output.to_csv(f'./data/analytics_dataempreendimento/analytics.csv', header=True, index=False)
    else:
        os.makedirs(f'./data/analytics_data/empreendimento/', exist_ok=True) 
        output.to_csv(f'./data/analytics_data/empreendimento/analytics.csv', header=True, index=False)
