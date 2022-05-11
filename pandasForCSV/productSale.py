import pandas as pd
df = pd.read_csv('./dataset/dataset.csv')
print(df)
#function aggregate_by_year
def aggregate_by_year():
    df = pd.read_csv('./dataset/dataset.csv')
    d = dict()
    for ind in df.index:
        if df['year'][ind] in d:
             d[df['year'][ind]]=d[df['year'][ind]]+df['sales'][ind]  
        else :
             d[df['year'][ind]]=df['sales'][ind]
    return d
 #function for aggregate_by_country                    
def aggregate_by_country():
    df = pd.read_csv('./dataset/dataset.csv')
    d = dict()
    for ind in df.index:
        if df['country'][ind] in d:
             d[df['country'][ind]]=d[df['country'][ind]]+df['sales'][ind]  
        else :
             d[df['country'][ind]]=df['sales'][ind]
    return d
#function for aggregate_by_category
def aggregate_by_category():
    df = pd.read_csv('./dataset/dataset.csv')
    d = dict()
    for ind in df.index:
        if df['category'][ind] in d:
             d[df['category'][ind]]=d[df['category'][ind]]+df['sales'][ind]  
        else :
             d[df['category'][ind]]=df['sales'][ind]
    return d
#call function and display return dict 
print("aggregate_by_year ",aggregate_by_year())
print("aggregate_by_country ",aggregate_by_country())
print("aggregate_by_category ",aggregate_by_category())
