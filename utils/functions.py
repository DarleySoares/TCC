import re

def format_area(df):
    if isinstance(df, str):
        return df.replace(".", "").replace(",", ".").split(" m²")[0]
    else:
        return 0

def format_categories(df):
    if isinstance(df, str):
        return df.split(" - ")[1]
    else:
        return 0

def format_garagem(df):
    return re.findall(r'\d+', df)[0]

def format_float(df):
    if isinstance(df, str):
        return df.replace(".", "").replace(",", ".")
    else:
        return 0

def format_percentage(df):
    if isinstance(df, str):
        return df.split("%")[0].replace(",", ".").strip()
    else:
        return 0
    
def format_coin(df):
    if isinstance(df, str):
        return df.split("R$ ")[1]
    else:
        return 0