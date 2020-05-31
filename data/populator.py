import pandas as pd

df = pd.read_csv("MSFT.csv")
#converting to pandas date for indexing
df['Date'] =  pd.to_datetime(data['Date'], format='%Y/%m/%d')
#sorting according to date
df = df.sort_values(by=['Date'], ascending=[True])

#indexing according to date
df.set_index('Date', inplace=True)

#populating data according to previous value
df = df.resample('D').ffill().reset_index()

#exporting to MSFT_complete
df.to_csv("MSFT_complete.csv")
