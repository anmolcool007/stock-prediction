import keys as keys
import tweepy
import csv
import pandas as pd
import random
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
md=pd.DataFrame(columns=['Date','Tweets'])
total=100
index=0
for index,row in data.iterrows():
    stre=row["Tweets"]
    my_new_string = re.sub('[^ a-zA-Z0-9]', '', stre)
    md.sort_index()
    md.set_value(index,'Date',row["Date"])
    md.set_value(index,'Tweets',my_new_string)
    index=index+1

