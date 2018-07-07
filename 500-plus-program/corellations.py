import pandas as pd
from scipy.stats import pearsonr 

# =============================================================================
# Compute pearson corellation (1 kid vs more kids in years)
# =============================================================================
def corellation_for_each_region(df):
    regions = pd.unique(df['region'])
    
    for i in range(len(regions)):
       print("{}: {}".format(regions[i],
             pearsonr(
                     [x for x in df[df['region']==regions[i]].values[:,2]],
                     [sum(x) for x in df[df['region']==regions[i]].values[:,3:12]]
                     )
                             )
             )  
             
def corellation_for_all_regions(df):   
    print("For all regions: {}".format(
         pearsonr(
                 [x for x in df.values[:,2]],
                 [sum(x) for x in df.values[:,3:12]]
                 )
                         )
         )   
         
def corellation_for_each_year(df):
    years = pd.unique(df['year'])
    
    for i in range(len(years)):
       print("{}: {}".format(years[i],
             pearsonr(
                     [x for x in df[df['year']==years[i]].values[:,2]],
                     [sum(x) for x in df[df['year']==years[i]].values[:,3:12]]
                     )
                             )
             )  
