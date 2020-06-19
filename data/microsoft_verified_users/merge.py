import pandas as pd
import pandas as pd
import nltk 
from nltk import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import re
from nltk.corpus import stopwords
stop = stopwords.words('english')
ps = PorterStemmer()
dft = pd.read_csv("translated.csv")
dates = dft.date.tolist()
dates = [str(dt).split()[0] for dt in dates]
tweets = dft.tweet.tolist()
new_dates = []
new_tweets = []
temp = str(tweets[0])
for i in range(1,len(dates)):
    if dates[i] == dates[i-1]:
        temp += str(tweets[i])
    else:
        new_tweets.append(temp)
        new_dates.append(dates[i-1])
        temp = str(tweets[i])

df = pd.DataFrame()
df['date'] = new_dates
df['tweet'] = new_tweets

#
#df['tweet'] = df['tweet'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
#df['tweet'] = df['tweet'].apply(lambda x: ' '.join([ps.stem(word) for word in x.split()]))


df.to_csv("merged.csv")
#print(df.head(10))
