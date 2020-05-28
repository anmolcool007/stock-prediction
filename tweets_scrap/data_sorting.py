import pandas as pd
import numpy as np
import re

data = pd.read_csv("Microsoft_Tweets.csv") 
md=pd.DataFrame(columns=['Date','Tweets'])
total=100
index=0
for index,row in data.iterrows():
    stre=row["Tweets"]
    pure_string = re.sub('[^ a-zA-Z0-9]', '', stre)
    md.sort_index()
    md.at[index,'Date']=row["Date"]
    md.at[index,'Tweets']=pure_string
    index=index+1

md['Date']=pd.to_datetime(md['Date'])
md.sort_values(by=['Date'])

md.to_csv(r'Microsoft_processed_tweets.csv')
