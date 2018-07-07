import pandas as pd
import numpy as np
 
# calculate each class probability   
def compute_class_priors(df, groupAttr):
    result = {}
    
    groups = df.groupby(groupAttr)
    for group in groups:
        result[group[0]] = len(group[1]) / len(df)
    
    return result

# calculate probabilities for given value in each class for each attribute
def compute_for_all_classes(data, groupAttr, attrs, new_example):
    result = {}
    groups = data.groupby(groupAttr)
  
    for group in groups:
        result[group[0]] = compute_for_all_attrs(group[1], attrs, new_example)
    
    return result

def compute_for_all_attrs(group, attrs, new_example):#attrs i new_example muszą miec taka sama kolejnosc atrybutow
    result = 1
   
    for attr in attrs:
       result *= compute_for_attr(group, attr, new_example[attr])

    return result
        
def compute_for_attr(group, attr, new_attr_value):  
    attr_groups = group.groupby(attr)
    
    for attr_value in attr_groups:
       if attr_value[0] == new_attr_value:
          return (len(attr_value[1]) / len(group))
    
    return 0
