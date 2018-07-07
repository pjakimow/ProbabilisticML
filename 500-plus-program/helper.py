import pandas as pd
import numpy as np

def set_default_value(df, index, def_value):
    column = df.iloc[:,index]
    column = column.tolist()
        
    for i in range(len(column)):
        if column[i]=='-':
            column[i]=def_value
            
    return pd.Series(column).astype(np.float64)
