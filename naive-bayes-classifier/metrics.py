import numpy as np

def accuracy(cm):
    cm_sum = np.sum(cm) # p + n
    rows_sum = np.sum(cm, axis=1) # tp + fn
    cols_sum = np.sum(cm, axis=0) # tp + fp
    
    result = []
    dim = len(rows_sum)
    for i in range(dim):
       result += [(cm_sum - rows_sum[i] - cols_sum[i] + 2 * cm[i, i]) / cm_sum]
    
    return result

def precision(cm):
    cols_sum = np.sum(cm, axis=0) # tp + fp
    
    result = []
    dim = len(cols_sum)
    for i in range(dim):
       result += [cm[i, i] / cols_sum[i]]
    
    return result

def recall(cm):
    rows_sum = np.sum(cm, axis=1) # tp + fn
    
    result = []
    dim = len(rows_sum)
    for i in range(dim):
       result += [cm[i, i] / rows_sum[i]]
    
    return result


def f1_measure(cm):
    pre = precision(cm)
    rec = recall(cm)
    
    result = []
    dim = len(pre)
    for i in range(dim):
       result += [2 * pre[i] * rec[i] / (pre[i] + rec[i])]
    
    return result
