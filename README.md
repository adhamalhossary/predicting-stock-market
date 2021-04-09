# Predicting Stock Market

## Introduction

The more I read about the stock market the more I realize how fascinating it can be. 
It is highly volatile, and there are several factors that can affect it, such as the overall state 
of the economy of different countries, government policies, media and many more. I always wondered 
if it is possible to build an algorithm that can take into account all of these different factors 
to make accurate forecasts on the price of different stocks. When I made the move to the data science
field, and the more I delved into machine learning I realised that people have been doing this for
some time! Different people use different methods such as supervised learning algorithms or neural
networks(LSTM is very hot when it comes to the stock market). This motivated me to make an initial 
attempt to build a machine learning model that can make accurate predictions on the future prices of
stocks.

## Data

For the purpose of this project I used data relating to the S&P500 index. The S&P500 is a great start as it aggregates the stock prices of the top 500 companies. The dataset used is `sphist.csv` which is in this repo. This dataset contains the price of the S&P index for every day from the year 1950 to 2015.

**Features**

- `Date`: The date of the record.


- `Open`: The opening price of the day (when trading starts).


- `High`: The highest trade price during the day.


- `Low`: The lowest trade price during the day.


- `Volume`: The number of shares traded.


- `Adj Close`: The daily closing price, adjusted retroactively to include any corporate actions. 

**Target Variable**

- `Close`: The closing price for the day (when trading is finished).

## Future Work

After testing different supervised learners, we deduced that the linear regression model had the highest performance when it came to speed and accuracy of predictions.
However, further exploration of different models could be done to find one that can provide better predictions. LSTM is known in the financial sector to provide very accurate predictions for stocks. It is a model that is definitely worth trying out in the future.

The data used to train the model was solely from the stock market itself, such as the closing price, and the volume of stocks traded.
It has been proven that the stock market is affected by news, and posts on social media 
such as Twitter and Facebook. This is due to how fast online news and media feeds travel in our time.
To build a more accurate model it is worth carrying out a sentiment analysis on both the news and 
social media, and feed that into the model to see if the accuracy of the predictions can be improved.