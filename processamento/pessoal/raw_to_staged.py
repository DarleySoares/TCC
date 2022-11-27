import pandas as pd
import numpy as np
import re
import os


def _preprocessing_raw_to_staged_pessoal(path: str) -> None:

    _path = path.replace('.', '_').replace(' ', '_')
    id = _path.split('_')[0]
    name = _path.split(f'{id}_')[1].split('.txt')[0]

    f = open(f'./data/raw_data/pessoal/{path}',  encoding='utf8', mode ='r')
    file = f.readlines()
    headers = [line.strip() for line in file]
    headers = [re.findall('^[1-9][A-ZÀ-Ú- ]+$|PROPOSTAS VINCULADAS+$', row)[0] for row in headers if re.findall('^[1-9][A-ZÀ-Ú- ]+$|PROPOSTAS VINCULADAS+$', row)]
    
    f.close()
    
    try:
        cut = headers.index("1 - IDENTIFICAÇÃO DA PROPOSTA")
        headers = headers[cut:]
        headers.insert(0, "IDENTIFICAO DA PROPOSTA")
        
        f = open(f'./data/raw_data/pessoal/{path}',  encoding='utf8', mode ='r')
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
                pass

        ranges = []
        start = 1
        try:
            end_test1 = headers.index("1 - IDENTIFICAÇÃO DA PROPOSTA", start+1)
            end_test2 = headers.index("PROPOSTAS VINCULADAS", start+1)
            end = min([end_test1, end_test2])
        except:
            end = len(headers)-1

        for index, value in enumerate(headers):
            
            ranges.append((start, end))
            
            if index == end-1 and end != len(headers)-1:
                try:
                    if abs(end_test1 - end_test2) == 1:
                        start =  max([end_test1, end_test2])
                    else:
                        start = end
                    
                    end_test1 = headers.index("1 - IDENTIFICAÇÃO DA PROPOSTA", start+1)
                    end_test2 = headers.index("PROPOSTAS VINCULADAS", start+1)
                    end = min([end_test1, end_test2])
                    
                except:
                    end = len(headers)-1

        ranges = list(dict.fromkeys(ranges))

        all_clientes = []
        for r in ranges:
            customer = parts[r[0]-1:r[1]-1]
            output = {}
            for row, pos in zip(customer, range(0, len(customer))):
                
                get_columns = row.split('\n')[1:]
                get_columns = [column.split('\t') for column in get_columns]        
                get_columns = [column for column in get_columns if column not in [['']]]
                get_columns = [np.array_split(column, 2) if len(column) == 4 else np.array(column) for column in get_columns]
                get_columns = [value if type(column) == list else column for column in get_columns for value in column]
                get_columns = [column.tolist() for column in get_columns]
                get_columns = [column for column in get_columns if len(column) > 1]
            
                seen = set()
                seen_add = seen.add
                
                get_columns =  [x for x in get_columns if not (x[0] in seen or seen_add(x[0]))]
                header = [column[0] for column in get_columns]
                values = [column[1] for column in get_columns]
                header = [h.replace(':', '') for h in header]
                data = dict(zip(header, values))
                output.update(data)
            
            output['ID'] = id
            output['Nome Arquivo'] = name
            all_clientes.append(output)

        append_dataframe = pd.DataFrame(all_clientes)

        if os.path.isfile(f'./data/staged_data/pessoal/{id}_{name}.csv'):
            append_dataframe.to_csv(f'./data/staged_data/pessoal/{id}_{name}.csv', mode='a', header=False, index=False)
        else:
            os.makedirs(f'./data/staged_data/pessoal/', exist_ok=True) 
            append_dataframe.to_csv(f'./data/staged_data/pessoal/{id}_{name}.csv', header=True, index=False)
    
    except:
        pass
