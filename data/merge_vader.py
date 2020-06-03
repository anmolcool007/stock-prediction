import pandas as pd

df = pd.read_csv("../sentiment_score/sentiment_score_vader.csv")
#take only date and sentiment score from the dataframe
df = df.loc[:, df.columns.intersection(['date','pos_vader','neg_vader','neu_vader','comp_vader'])]

#conveert string into date time
df['date'] =  pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')

#taking average based on same date
df = df.set_index('date').groupby(pd.Grouper(freq='d')).mean().dropna(how='all')

#populating missing data
df = df.resample('D').ffill().reset_index()

df1 = pd.read_csv("MSFT_complete.csv")

#new column in stock data (sentiment score column)
df1['pos_vader'] = df['pos_vader']
df1['neg_vader'] = df['neg_vader']
df1['neu_vader'] = df['neu_vader']
df1['comp_vader'] = df['comp_vader']
print(df1)
df1.to_csv("MSFT_with_vader_sentiment.csv")
