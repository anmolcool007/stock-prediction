import pandas as pd
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

df = pd.read_csv("../../data/microsoft_verified_users/merged.csv")

tweets = df.tweet.tolist()

vader_sentiment = []
start = time.time()
for tweet in tweets:
    print(time.time()-start,"sec")
    vader_sentiment.append(analyzer.polarity_scores(tweet)['compound'])

df['vader_sentiment'] = vader_sentiment

df.to_csv("verified_user-vader_sentiment.csv")
