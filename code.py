import pandas as pd  
data = {'Name':['Tom', 'Jack', 'nick', 'juli'], 
'Age':[40, 11, 78, 28]} 
df = pd.DataFrame(data=data) 
df['Hobby'] = ['Football', 'Video Games', 'Reading', 'Running'] 
print(df) 
df.to_csv('data/df.csv')