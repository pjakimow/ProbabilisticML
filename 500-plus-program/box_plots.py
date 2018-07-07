import pandas as pd
import matplotlib.pyplot as plt

        
def show_region(df, region_nr):
    regions = pd.unique(df['region'])
    name = regions[region_nr]
    data = df[df['region']==regions[region_nr]]
    
    y = []
    for i in range(2, 12):
        y+=[data.iloc[:,i].tolist()]
    
    fig, ax = plt.subplots()
    ax.boxplot(y)
    ax.set_title(name)
    ax.set_xlabel('Minimalna liczba dzieci w rodzinie')
    ax.set_ylabel('Liczba rodzin')
    plt.show()
    #print(y)

def show_regions_on_separated_plots(df):
    for i in range(0, 16):
        show_region(df, i)    
  
def all_regions_jth_child(df, j): 
    regions = pd.unique(df['region'])

    y = []
    for i in range(0, 16):
        y += [[x for x in df[df['region']==regions[i]].values[:,j+1]]]
    
    fig, ax = plt.subplots()
    ax.boxplot(y,labels=regions)
    ax.set_title('{}. dziecko w rodzinie'.format(j))
    ax.set_xlabel('Województwo')
    ax.set_ylabel('Liczba urodzeń')
    plt.xticks(rotation=30)
    plt.show()
    #print(y)
    
# =============================================================================
def all_years_more_than_1(df): 
    y = []
    for i in range(2002, 2017):
        y += [[sum(x) for x in df[df['year']==i].values[:,3:12]]]
    
    fig, ax = plt.subplots()
    labels = list(range(2002, 2017))
    ax.boxplot(y,labels=labels)
    ax.set_title('Wszystkie wojewodztwa razem')
    ax.set_xlabel('Rok')
    ax.set_ylabel('Liczba urodzeń powyżej 1 dziecka')
    plt.show()
    #print(y)
  
def all_years_jth_child(df,j): 
    y = []
    for i in range(2002, 2017):
        y += [[x for x in df[df['year']==i].values[:,j+1]]]
    
    fig, ax = plt.subplots()
    labels = list(range(2002, 2017))
    ax.boxplot(y,labels=labels)
    ax.set_title('Wszystkie wojewodztwa razem')
    ax.set_xlabel('Rok')
    ax.set_ylabel('Liczba urodzeń {}. dziecka'.format(j))
    plt.show()
    #print(y)
        
def all_years_all_regions(df): 
    y = []
    for i in range(2002, 2017):
        data = df[df['year']==i].values[:,1]
        
        y += [[x for x in data]]
    
    fig, ax = plt.subplots()
    labels = list(range(2002, 2017))
    ax.boxplot(y,labels=labels)
    ax.set_title('Wszystkie wojewodztwa razem')
    ax.set_xlabel('Rok')
    ax.set_ylabel('Liczba urodzeń')
    plt.show()
    #print(y)
    
def before_and_after_program_jth_child(df,j): 
    y = []
    for i in range(2002, 2017):
        y += [[x for x in df[df['year']==i].values[:,j+1]]]
            
    before = [sum(x)/len(x) for x in zip(y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9], y[10], y[11], y[12], y[13],)]
    after = y[14]
    
    fig, ax = plt.subplots()
    labels = ['2002-2015\nsrednia', '2016']
    ax.boxplot([before, after],labels=labels)
    ax.set_title('Wszystkie wojewodztwa razem')
    ax.set_xlabel('Rok')
    ax.set_ylabel('Liczba urodzeń {}. dziecka'.format(j))
    plt.show()
    #print(y)
    
def years_2015_2016_jth_child(df,j): 
    y = []
    for i in range(2015, 2017):
        y += [[x for x in df[df['year']==i].values[:,j+1]]]
    
    fig, ax = plt.subplots()
    labels = [2015, 2016]
    ax.boxplot(y,labels=labels)
    ax.set_title('Wszystkie wojewodztwa razem')
    ax.set_xlabel('Rok')
    ax.set_ylabel('Liczba urodzeń {}. dziecka'.format(j))
    plt.show()
    #print(y)