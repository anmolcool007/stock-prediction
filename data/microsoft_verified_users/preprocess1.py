import pandas as pd
import re

fields = ['date','tweet']
df = pd.read_csv("microsoft_verified_tweets.csv",dtype=str,usecols=fields)


 
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"http\S+", "", str(x)))
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"www.+", "", str(x)))


df['tweet'] = df['tweet'].apply(lambda x: re.sub("#", "", str(x)))
df['tweet'] = df['tweet'].apply(lambda x: re.sub("@", "", str(x)))
df['tweet'] = df['tweet'].apply(lambda x: re.sub("\n", "", str(x)))
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"pic.twitter.com/+", "",str(x) ))

df.to_csv("mixedlang.csv")
