from textblob import TextBlob
import pandas as pd

print("---reading csv file---")
df = pd.read_csv("../preprocess/processed_tweets.csv")

print("---calculating sentiment using textblob---")
df['textblob_sentiment'] = df['tweet'].apply(lambda x:TextBlob(x).sentiment.polarity)

print("---saving in csv file---")
df.to_csv("sentiment_score_textblob.csv")