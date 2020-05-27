import keys as keys
import tweepy
import pandas as pd
import numpy as np

ck = keys.consumer_key
csk = keys.consumer_secret_key
at = keys.access_token
ast = keys.access_secret_token

auth = tweepy.OAuthHandler(ck, csk)
auth.set_access_token(at, ast)
api = tweepy.API(auth,wait_on_rate_limit=True)

fetch_tweets=tweepy.Cursor(api.search, q="#Microsoft",count=100, lang ="en",since="2020-03-01", tweet_mode="extended").items()
data=pd.DataFrame(data=[[tweet_info.created_at.date(),tweet_info.full_text]for tweet_info in fetch_tweets],columns=['Date','Tweets'])


data.to_csv("Microsoft_Tweets.csv")