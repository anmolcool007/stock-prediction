import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

df = pd.read_csv("merged.csv")
sentiment = []
tweets = df.tweet.tolist()
dates = df.date.tolist()
# print(len(df),len(df1))

for i in range(len(df)):
    sentiment.append(analyser.polarity_scores(tweets[i])['compound'])
df['sentiment'] = sentiment
df.to_csv("scores.csv")