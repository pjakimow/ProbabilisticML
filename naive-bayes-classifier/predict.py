import pandas as pd
import numpy as np
import operator
import probabilities as pr

def predict(data, groupAttr, learningAttrs, new_example):
    priors = pr.compute_class_priors(data, groupAttr)
    probs = pr.compute_for_all_classes(data, groupAttr, learningAttrs, new_example)
    results = {}
    
    for group in [key for key, value in data.groupby(groupAttr)]:
        results[group] = priors[group] * probs[group]
    
#    print("\nPredict: \n {}".format(results))   
    return  max(results.items(),  key=operator.itemgetter(1))
