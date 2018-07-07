import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB

from predict import predict
import helper
import probabilities as pr
import metrics

def run_my_classifier(data):
    groupAttr = 'class'
    attrs = data.columns.values[:-1]
    
    train, test = train_test_split(data, test_size=0.2, shuffle=True)
    
    y_pred = {}
    y_true = test[groupAttr].to_dict()
    
    for index, test_example in test.iterrows():
        y_pred[index], _ = predict(train, groupAttr, attrs, test_example)
    
    count = 0
    for key in y_pred.keys():
    #    print("true: {}, pred: {}".format(y_true[key], y_pred[key]))
        if y_pred[key] == y_true[key]:
            count +=1
    
    print("Correct predicted: {} of all {}".format(count, len(y_pred)))
    
    report = classification_report(list(y_true.values()), list(y_pred.values()), target_names=helper.get_groups_names(data, groupAttr))
    print(report)
    
    cmat = confusion_matrix(list(y_true.values()), list(y_pred.values()))
    accs = metrics.accuracy(cmat)
    print("accuracy: {}".format([round(item,2) for item in accs]))
    print("mean accuracy: {}".format(np.mean(accs)))
    print("priors: {}".format(pr.compute_class_priors(data, groupAttr)))

def remap_car_attrs(data):
    di = {'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}
    data = helper.remap_dataframe_column(data, 'buying_price', di)
    data = helper.remap_dataframe_column(data, 'maint_price', di)
    
    di = {'2': 2, '3':3, '4': 4, '5more': 5}
    data = helper.remap_dataframe_column(data, 'doors', di)
    
    di = {'2': 2, '4': 4, 'more': 5}
    data = helper.remap_dataframe_column(data, 'persons', di)
    
    di = {'small': 0, 'med': 1, 'big': 2}
    data = helper.remap_dataframe_column(data, 'lug_boot', di)

    di = {'low': 0, 'med':1, 'high':2}
    data = helper.remap_dataframe_column(data, 'safety', di)
    
    return data

def run_sklearn_classifier(data):
    
    data = remap_car_attrs(data)
    
    #split data and shuffle
    train, test = train_test_split(data, test_size=0.2, shuffle=True)
    
    X_train = train.iloc[:, 0:6]
    y_train = train.iloc[:, 6]
    
    X_test = test.iloc[:, 0:6]
    y_test = test.iloc[:, 6]
    
    #priors = [0.2222, 0.0399, 0.7002, 0.0376]
    priors = [0.2, 0.15, 0.5, 0.15]
    nb = MultinomialNB(class_prior = priors, fit_prior=False)
    nb.fit(X_train, y_train)
    
    y_pred = nb.predict(X_test)
    y_test = np.asarray(y_test.values.tolist())
          
    print("Correct predicted: {} of all {}".format(sum(y_test == y_pred), len(y_pred)))
    
    report = classification_report(y_test, y_pred)
    print(report)
    
    cmat = confusion_matrix(y_test, y_pred)
    accs = metrics.accuracy(cmat)
    print("accuracy: {}".format([round(item,2) for item in accs]))
    print("mean accuracy: {}".format(np.mean(accs)))
    print("y_train size: {}".format(len(y_train)))
    print("y_train unacc number: {}".format(sum(y_train == 'unacc')))
    print("priors: {}".format(nb.class_prior))
    print(nb.class_log_prior_)

data = pd.read_table('data/car.data', sep=',')    
run_my_classifier(data)
#run_sklearn_classifier(data)