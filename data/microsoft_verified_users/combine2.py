import pandas as pd


#read stock data
df1 = pd.read_csv("../MSFT_complete.csv")
#read sentiment_score
df = pd.read_csv("../../sentiment_score/Verified_user/verified_user-vader_sentiment.csv")

#new column in stock data (making sure number of rows in df and df1 are same)
df1['vader_sentiment'] = df['vader_sentiment']

df1.to_csv("verified_MSFT-vader.csv")
