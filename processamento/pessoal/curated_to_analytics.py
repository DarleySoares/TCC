import os
import pandas as pd
pd.options.mode.chained_assignment = None

from utils.constants_pessoal import COLUMNS_ANALYTICS, float_columns, percentage_columns, categories_columns
from utils.functions import format_float, format_percentage, format_categories


def _preprocessing_curated_to_analytics_pessoal() -> None:
    
    output = pd.read_csv(f'./data/curated_data/pessoal/dados_pessoal.csv')
    output = output[COLUMNS_ANALYTICS.keys()]


    for column in float_columns:
        output[column] = output.apply(lambda df: format_float(df[column]), axis = 1)
        
    for column in percentage_columns:
        output[column] = output.apply(lambda df: format_percentage(df[column]), axis = 1)

    for column in categories_columns:
        output[column] = output.apply(lambda df: format_categories(df[column]), axis = 1)
        
    for column, typ in COLUMNS_ANALYTICS.items():

        if typ in [float, int]:
            output[column] = output[column].fillna(0)
        output[column] = output[column].astype(typ)

    
    if os.path.isfile(f'./data/analytics_data/pessoal/analytics.csv'):
        output.to_csv(f'./data/analytics_data/pessoal/analytics.csv', header=True, index=False)
    else:
        os.makedirs(f'./data/analytics_data/pessoal/', exist_ok=True) 
        output.to_csv(f'./data/analytics_data/pessoal/analytics.csv', header=True, index=False)
