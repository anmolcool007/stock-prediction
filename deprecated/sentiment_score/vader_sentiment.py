from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd    

from textblob import TextBlob
import pandas as pd

print("---reading csv file---")
df = pd.read_csv("../preprocess/processed_tweets.csv")
analyzer = SentimentIntensityAnalyzer()
print("---calculating sentiment using vader---")
tweets = df['tweet'].tolist()
sentiment = []
for tweet in tweets:
    sentiment.append(analyzer.polarity_scores(tweet))
sentiment = pd.DataFrame(sentiment)
df['pos_vader'] = sentiment.pos
df['neg_vader'] = sentiment.neg
df['neu_vader'] = sentiment.neu
df['comp_vader'] = sentiment.compound

df.to_csv("sentiment_score_vader.csv")