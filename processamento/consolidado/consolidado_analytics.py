import pandas as pd
import os


def _processing_analytics():
    
    empreendimento = pd.read_csv(f'./data/analytics_data/empreendimento/analytics.csv')
    pessoal = pd.read_csv(f'./data/analytics_data/pessoal/analytics.csv')
    incc = pd.read_csv(f'./data/curated_data/diversos/incc.csv')

    incc["ano"] = incc["incc_data_cadastro"].apply(lambda x: x.split("/")[1])
    incc["mes"] = incc["incc_data_cadastro"].apply(lambda x: x.split("/")[0])
    incc["ano"] = incc["ano"].astype(int)
    incc["mes"] = incc["mes"].astype(int)

    output = pd.merge(pessoal, empreendimento, how = "left", left_on = ["cd_grh", "tp_unidade"], right_on= ["cd_grh", "tp_unidade"])

    output = output[output.id_y.notnull()]
    output = output[output.dt_avaliacao.notnull()]

    output["ano"] = output["dt_avaliacao"].apply(lambda x: x.split("/")[2])
    output["mes"] = output["dt_avaliacao"].apply(lambda x: x.split("/")[1])
    output["ano"] = output["ano"].astype(int)
    output["mes"] = output["mes"].astype(int)

    output = pd.merge(output, incc, how = "left", on=["ano", "mes"])
    
    if os.path.isfile(f'./data/analytics_data/consolidado/analytics.csv'):
        output.to_csv(f'./data/analytics_data/consolidado/analytics.csv', header=True, index=False)
    else:
        os.makedirs(f'./data/analytics_data/consolidado/', exist_ok=True) 
        output.to_csv(f'./data/analytics_data/consolidado/analytics.csv', header=True, index=False)
