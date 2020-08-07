import pandas as pd
import re

df = pd.read_csv("#msft.csv",usecols=['date','tweet'])
# print(df)
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"http\S+", "", str(x)))
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"www.+", "", str(x)))


df['tweet'] = df['tweet'].apply(lambda x: re.sub("#", "", str(x)))
df['tweet'] = df['tweet'].apply(lambda x: re.sub("@", "", str(x)))
df['tweet'] = df['tweet'].apply(lambda x: re.sub("\n", "", str(x)))
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"pic.twitter.com/+", "",str(x) ))

df.to_csv("mixedlang.csv")
