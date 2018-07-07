import pandas as pd
import box_plots as bp
import corellations as cor
import helper

# prepare data
data=pd.DataFrame()
for year in range(2002, 2016+1):
    temp=pd.read_csv('datasets/regions_pl_uro_{}_00_2p.csv'.format(year))
    
    #remove additional columns
    temp=temp.iloc[:,1:14]
    
    #add year column
    rows=len(temp)
    temp['year'] = pd.Series([year]*rows)
    
    #update result dataframe
    data=data.append(temp, ignore_index=True)

data['region'] = [x.strip() for x in data['region']]

data.iloc[:,12]=helper.set_default_value(data, 12, 0)
data.iloc[:,10]=helper.set_default_value(data, 10, 0)

# run tests
cor.corellation_for_each_region(data)
cor.corellation_for_each_year(data)