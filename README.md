# Stock-Prediction [![Python Versions](https://img.shields.io/pypi/pyversions/yt2mp3.svg)](https://pypi.python.org/pypi/yt2mp3/) 
Twitter Sentiment Analysis to improve Stock Price Prediction using LSTM
## Description

Stock market prediction has always been a challenge in our society, every year computational analysts and data scientists try to understand this huge volatile chunk with millions of data using their techniques and models to predict a trend which work only under certain factors with limited accuracy. The result becomes interesting when you take many factors into account while trying to get sensible results over plethora of related data from unrelated fields.

## Introduction

In this project we attempt to predict the behaviour of the stock market by using time-series data while incorporating other environmental factors in the neural network architecture - Long Short Term Memory(LSTM). These environmental factors are not mentioned in previous stock data, they just affect the result eg: disease outbreak , change of government etc. understanding these factors and their effect on the stock prices can improve the stock estimation drastically. We aim to vary the weights of our network by these data and see how it matches with the previous result. 

## Installation

### Clone

- Clone this repo to your local machine using `https://github.com/anmolcool007/stock-prediction`

### Setup

- Virtual Environment

```shell
$ pip install virtualenv
$ virtualenv <env_name>
```
>Mac OS / Linux
```shell
$ source <env_name>/bin/activate
```
>Windows
```shell
$ <env_name>\Scripts\activate
```

- Packages

```shell
$ pip install <packages from requirements.txt>
```
---
## Technology Stack
- Python
- Numpy
- Pandas
- Matplotlib
- Tensorflow
- Keras
- Twitter API
- Google API
- sklearn

## Components

### Tweet Scraping
- Using Web Scraping techniques 
- Monitoring and organization using open source third party program <a href="https://github.com/scrapy/scrapy" target="_blank">Scrapy</a>.

### Pre-Processing
- Combining tweets according to date using Pandas
- Google API to convert other native language in english
- Removing links through RegEx
- Removing mentions and "#" from the word

### Sentiment Analysis
- Use of pre-trained open source sentiment analyzer <a href="https://github.com/cjhutto/vaderSentiment" target="_blank">Vader</a>.
- Filling void using interpolation.
---

## Training Model

### LSTM model training
- Define Model 
- Set hyperparameters
- Log the output

## Result

### Graph  
- Original closing price : Blue
- Only LSTM based predicted price : Orange
- LSTM with sentiment based predicted price : Green

<img src="https://github.com/anmolcool007/stock-prediction/blob/master/closing-price_comparision.png" title="Results">

### Comparision

| Metric | LSTM | LSTM + Sentiment |
| --- | --- | --- |
| **R2 Score** | 0.883 | 0.987 |
| **MSE** | 0.0021304 | 0.0002669 |

---

## Contributors

- <a href="https://github.com/Yash5044" target="_blank">Yash Chaubey</a>
- <a href="https://github.com/anmolcool007" target="_blank">Anmol Gupta</a>
