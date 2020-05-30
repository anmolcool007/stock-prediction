import pandas as pd 
data = pd.read_csv("microsoft_final.csv")
data['reply_to'] = data['reply_to'].astype('str')
mask = (data['reply_to'].str.len() == 50)
data = data.loc[mask]
data = data.loc[:, data.columns.intersection(['date','tweet'])]
data.to_csv("filtered_microsoft.csv")
