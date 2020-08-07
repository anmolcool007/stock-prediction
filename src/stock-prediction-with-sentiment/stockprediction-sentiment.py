import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import tensorflow as tf
from time import time
from keras.models import Sequential, load_model
from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.layers import LSTM
from keras.optimizers import Adam
from time import time
from keras.callbacks import EarlyStopping
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()

df = pd.read_csv("../../data/microsoft_verified_users/verified_MSFT-vader.csv",parse_dates=True,index_col="Date")
# df = df[1563:]
print(df.corr()['Close'])
del df["Unnamed: 0"]
del df["Unnamed: 0.1"]
df.drop(columns=['Volume','Adj Close'],inplace=True)
df.columns = [['open', 'high', 'low','close','sentiment']]
print("---dataframe head---")
print(df.head())

print("--scaling data---")
data = sc.fit_transform(df) 
train_ind = int(0.6*len(df))
val_ind = train_ind + int(0.2*len(df))

train = data[:train_ind]
val = data[train_ind:val_ind]
test = data[val_ind:]

print("--shapes--")
print("train,test,val",train.shape, test.shape, val.shape)

xtrain,ytrain,xval,yval,xtest,ytest = train[:,:5],train[:,3],val[:,:5],val[:,3],test[:,:5],test[:,3]

lookback = 60
n_features = 5
train_len = len(xtrain) - lookback
test_len = len(xtest) - lookback
val_len = len(xval) - lookback

x_train = np.zeros((train_len, lookback, n_features))
y_train = np.zeros((train_len))
for i in range(train_len):
    ytemp = i+lookback
    x_train[i] = xtrain[i:ytemp]
    y_train[i] = ytrain[ytemp]
print("x_train", x_train.shape)
print("y_train", y_train.shape)

x_test = np.zeros((test_len, lookback, n_features))
y_test = np.zeros((test_len))
for i in range(test_len):
    ytemp = i+lookback
    x_test[i] = xtest[i:ytemp]
    y_test[i] = ytest[ytemp]
print("x_test", x_test.shape)
print("y_test", y_test.shape)

x_val = np.zeros((val_len, lookback, n_features))
y_val = np.zeros((val_len))
for i in range(val_len):
    ytemp = i+lookback
    x_val[i] = xval[i:ytemp]
    y_val[i] = yval[ytemp]
print("x_val", x_val.shape)
print("y_val", y_val.shape)

model = Sequential()  
model.add(LSTM(600,input_shape = (lookback, n_features), return_sequences=True))
model.add(LSTM(700))
model.add(Dropout(0.15))
model.add(Dense(1))
print(model.summary())

model.compile(loss = 'mse', optimizer = 'adam')
earlystop = EarlyStopping(monitor='val_loss', min_delta=0.0001, patience=80,  verbose=1, mode='min')

start = time()
print("start:",0)
history = model.fit(x_train,y_train, epochs = 100, batch_size=30, 
          validation_data=(x_val,y_val),verbose = 1, 
          shuffle = False, callbacks=[earlystop])
print("endtime:",time()-start)

<<<<<<< HEAD
model.save("./models/model_vader7.h5")
loss = history.history
plt.plot(loss['loss'])
plt.plot(loss['val_loss'])
plt.savefig("./plots/loss_vader7.jpg")
=======
model.save("./models/model_vader6.h5")
loss = history.history
plt.plot(loss['loss'])
plt.plot(loss['val_loss'])
plt.savefig("./plots/loss_vader6.jpg")
>>>>>>> 7bf5ab529d185e0cc646bfcf14a8abb1ed7a4042
plt.show()
# model = load_model("./models/model_vader1.h5")
y_pred = model.predict(x_test)
# print(model.summary())


plt.figure(figsize=(20,10))
plt.plot( y_test, '.-', color='red', label='Real values', alpha=0.5)
plt.plot( y_pred, '.-', color='blue', label='Predicted values', alpha=1)
<<<<<<< HEAD
plt.savefig("./plots/result_vader7.jpg")
=======
plt.savefig("./plots/result_vader6.jpg")
>>>>>>> 7bf5ab529d185e0cc646bfcf14a8abb1ed7a4042
plt.show()

print("r2_score:",r2_score(y_pred,y_test))



