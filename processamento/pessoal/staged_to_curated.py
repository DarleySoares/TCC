import pandas as pd
import os

from utils.constants_pessoal import COLUMNS_CURATED

def _preprocessing_staged_to_curated_pessoal(path:str) -> None:
    
    id = path.split('_')[0]
    name = path.split(f'{id}_')[1]
    
    columns = COLUMNS_CURATED.keys()
    new_columns = COLUMNS_CURATED.values()
    try:
        output = pd.read_csv(f'./data/staged_data/pessoal/{id}_{name}')
        
        none_columns = list(set(columns) - set(output.columns))
        
        for col in none_columns:
            output[col] = None
            
        output = output[columns]
        output.columns = new_columns

        if os.path.isfile(f'./data/curated_data/pessoal/dados_pessoal.csv'):
            output.to_csv(f'./data/curated_data/pessoal/dados_pessoal.csv', mode='a', header=False, index=False)   
        else:
            os.makedirs(f'./data/curated_data/pessoal/')
            output.to_csv(f'./data/curated_data/pessoal/dados_pessoal.csv', header=True, index=False)
                
    except:
        pass
        

def _preprocessing_drop_duplicates_curated_pessoal(path:str) -> None:
    
    output = pd.read_csv(f'./data/curated_data/pessoal/{path}')
    output = output.drop_duplicates()
    output.to_csv(f'./data/curated_data/pessoal/{path}', header=True, index=False)
