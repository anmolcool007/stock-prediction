import pandas as pd

df = pd.read_csv("../sentiment_score/sentiment_score_vader.csv")
#take only date and sentiment score from the dataframe
df = df.loc[:, df.columns.intersection(['date','textblob_sentiment'])]

#conveert string into date time
df['date'] =  pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')

#taking average based on same date
df = df.set_index('date').groupby(pd.Grouper(freq='d')).mean().dropna(how='all')

#populating missing data
df = df.resample('D').ffill().reset_index()

df1 = pd.read_csv("MSFT_complete.csv")

#new column in stock data (sentiment score column)
df1['textblob_sentiment'] = df['textblob_sentiment']
df1.to_csv("MSFT_with_sentiment.csv")
