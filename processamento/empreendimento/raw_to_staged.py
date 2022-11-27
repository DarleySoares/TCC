import pandas as pd
import numpy as np
import re
import os


def _preprocessing_raw_to_staged_empreendimento(path: str) -> None:

    _path = path.replace('.', '_').replace(' ', '_')
    id = _path.split('_')[0]
    name = _path.split(f'{id}_')[1].split('.txt')[0]

    f = open(f'./data/raw_data/empreendimento/{path}',  encoding='utf8', mode ='r')
    file = f.readlines()
    
    headers = [re.findall('^[A-ZÀ-Ú- ]+$', row)[0] for row in file if re.findall('^[A-ZÀ-Ú- ]+$', row)]

    f.close()

    f = open(f'./data/raw_data/empreendimento/{path}',  encoding='utf8', mode ='r')
    file = f.read()

    parts = []
    for pos in range(0, len(headers)):
        try:
            if pos == 0:
                part = file.split(headers[pos+1], 1)[0]
                rest = file.split(headers[pos+1], 1)[1]
            else:
                part = rest.split(headers[pos+1], 1)[0]
                rest = rest.split(headers[pos+1], 1)[1]
                        
            parts.append(part)
                
        except:
            if headers[pos] in ['TIPOS DE UNIDADES', 'QUANTIDADE DE UNIDADES']:
                parts.append(rest)
            pass

    for row, pos in zip(parts, range(0, len(parts))):

        if pos == 0:
            get_columns = row.split('\n')[1:]
        else:
            get_columns = row.split('\n')
                
        get_columns = [column.split('\t') for column in get_columns]        
        get_columns = [column for column in get_columns if column not in [['']]]
        get_columns = [np.array_split(column, 2) if len(column) == 4 else np.array(column) for column in get_columns]
        get_columns = [value if type(column) == list else column for column in get_columns for value in column]
        get_columns = [column.tolist() for column in get_columns]
        
        seen = set()
        seen_add = seen.add
        
        if headers[pos] != 'TIPOS DE UNIDADES':
            get_columns =  [x for x in get_columns if not (x[0] in seen or seen_add(x[0]))]
            header = [column[0] for column in get_columns]
            values = [column[1] for column in get_columns]
            header = [h.replace(':', '') for h in header]
            data = dict(zip(header, values))
            data['ID'] = id
            data['Nome Arquivo'] = name
            append_dataframe = pd.DataFrame(data, index = [0])
          
        else:
            header = get_columns[2]
            values = get_columns[2:-1]
            
            append_dataframe = pd.DataFrame(data = values, columns= header)
            append_dataframe = append_dataframe.drop_duplicates()
            append_dataframe = append_dataframe.drop(index = 0)
            append_dataframe = append_dataframe.reset_index(drop=True)
            append_dataframe['ID'] = id
            append_dataframe['Nome Arquivo'] = name
            append_dataframe = append_dataframe[append_dataframe['TIPO DE IMÓVEL'] != 'Total']

        if headers[pos] == 'DADOS DO EMPREENDIMENTO' and pos <= 3:
            filename = 'DADOS DO EMPREENDIMENTO GERAL'
        else:
            filename = headers[pos]
            
        if os.path.isfile(f'./data/staged_data/empreendimento/{id}_{name}/{filename}.csv'):
            append_dataframe.to_csv(f'./data/staged_data/empreendimento/{id}_{name}/{filename}.csv', mode='a', header=False, index=False)
        else:
            os.makedirs(f'./data/staged_data/empreendimento/{id}_{name}/', exist_ok=True) 
            append_dataframe.to_csv(f'./data/staged_data/empreendimento/{id}_{name}/{filename}.csv', header=True, index=False)
