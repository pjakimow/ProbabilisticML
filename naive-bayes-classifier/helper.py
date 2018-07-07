import pandas as pd

def get_groups_names(data, groupAttr):   
    groups= data.groupby(groupAttr).groups   
    return list(groups.keys())

def remap_dataframe_column(df, col_name: int, new_values: dict):
  return df.replace({col_name: new_values})