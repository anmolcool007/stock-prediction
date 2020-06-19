import pandas as pd
import nltk 
from nltk import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import re
from nltk.corpus import stopwords
from textblob import TextBlob

stop = stopwords.words('english')
ps = PorterStemmer()
lmtzr = WordNetLemmatizer()
df = pd.read_csv('../tweets_scrap/filter/filtered_microsoft.csv')
del df['Unnamed: 0']

temp = []
for i in range(len(df)):
    temp.append(i+1)
df['id'] = temp
df = df[['id','date','tweet']]

print("---Removing Links---")
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"http\S+", "", x))
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"www.+", "", x))

print("---Removing Hastags/Usernames---")
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"#", "", x))
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"@+", "", x))


print("---Removing Stop Words ---")
df['tweet'] = df['tweet'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

print("---Stemming---")
df['tweet'] = df['tweet'].apply(lambda x: ' '.join([ps.stem(word) for word in x.split()]))

# print("---Lemmetizing---")
# df['tweet'] = df['tweet'].apply(lambda x: ' '.join([lmtzr.lemmatize(word,'v') for word in x.split()]))

# print("--Spelling Checker---")
# df['tweet'] = df['tweet'].apply(lambda x: TextBlob(x).correct())

print("---Saving to CSV file---")
df.to_csv("processed_tweets.csv")

