import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
dft = pd.read_csv("translated.csv")
date = dft.date.tolist()
date = [str(dt).split()[0] for dt in date]
tweet = dft.tweet.tolist()
tweets = []
dates = []
new_dates = []
new_tweets = []
for i in range(len(dft)):
    if len(date[i].split("-")[0])==4:
        dates.append(date[i])
        tweets.append(tweet[i])
temp = str(tweets[0])
for i in range(1,len(dates)):
    if dates[i] == dates[i-1]:
        temp +=". " + str(tweets[i])
    else:
        new_tweets.append(temp)
        new_dates.append(dates[i-1])
        temp = str(tweets[i])

df = pd.DataFrame()
df['date'] = new_dates
df['tweet'] = new_tweets

df.to_csv("merged.csv")