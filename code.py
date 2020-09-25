import pandas as pd  
data = {'Name':['Tom', 'Jack', 'nick', 'juli'], 
'Age':[40, 11, 78, 28]} 
df = pd.DataFrame(data=data) 
print(df) 
# df['Hobby'] = ['Football', 'Video Games', 'Reading', 'Running'] 
df.to_csv('data/df.csv')