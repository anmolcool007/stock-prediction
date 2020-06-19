import pandas as pd


#read stock data
df1 = pd.read_csv("../MSFT_complete.csv")
#read sentiment_score
df = pd.read_csv("../../sentiment_score/Verified_user/verified_user-sentiment_score_textblob.csv")

#new column in stock data (making sure number of rows in df and df1 are same)
df1['textblob_sentiment'] = df['textblob_sentiment']

df1.to_csv(r"verified_MSFT-textblob.csv")
