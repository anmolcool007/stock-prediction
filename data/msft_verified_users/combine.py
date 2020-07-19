import pandas as pd

df1 = pd.read_csv("../MSFT_complete.csv")
df2 = pd.read_csv("scores.csv")
df1 = df1[2655:]
df2 = df2[33:]
sentiment = df2.sentiment.tolist()
sentiment.reverse()
# for i in range(1,len(sentiment)):
#     sentiment[i] += sentiment[i-1]
# print(df1)
df1['sentiment'] = sentiment

# df1.to_csv("final.csv")

print(df1[:30].tail())
# print(df1.corr()['Close'])