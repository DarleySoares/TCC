import pandas as pd
import os

from utils.constants_empreendimento import COLUMNS_CURATED, RENAME_COLUMNS_CURATED

def _preprocessing_staged_to_curated_empreendimento(path:str) -> None:
    
    id = path.split('_')[0]
    name = path.split(f'{id}_')[1]
    
    for old, new in zip(COLUMNS_CURATED.items(), RENAME_COLUMNS_CURATED.items()):
        
        key = old[0]
        columns = old[1]
        new_columns = new[1]
        try:
            output = pd.read_csv(f'./data/staged_data/empreendimento/{id}_{name}/{key}.csv')
            
            none_columns = list(set(columns) - set(output.columns))
            
            for col in none_columns:
                output[col] = None
                
            output = output[columns]
            output.columns = new_columns
        
            if os.path.isfile(f'./data/curated_data/empreendimento/{key}/{key}.csv'):
                output.to_csv(f'./data/curated_data/empreendimento/{key}/{key}.csv', mode='a', header=False, index=False)   
            else:
                os.makedirs(f'./data/curated_data/empreendimento/{key}/')
                output.to_csv(f'./data/curated_data/empreendimento/{key}/{key}.csv', header=True, index=False)
                
        except:
            if key not in ['DADOS ADICIONAIS', 'DADOS DA PRÉ-CONTRATAÇÃO']:
                print(id,' - ', name, ' - ', key)
            pass
        

def _preprocessing_drop_duplicates_curated_empreendimento(path:str) -> None:
    
    output = pd.read_csv(f'./data/curated_data/empreendimento/{path}/{path}.csv')
    output = output.drop_duplicates()
    output.to_csv(f'./data/curated_data/empreendimento/{path}/{path}.csv', header=True, index=False)
