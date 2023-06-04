# -*- coding: utf-8 -*-
# Copyright 2023 by Streamlit Inc.

"""An example of showing live Bitcoin prices and forecasting."""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Bitcoin Price Forecaster", page_icon=":moneybag:")

# API parameters
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'your_api_key',
}

session = Session()
session.headers.update(headers)

@st.cache(show_spinner=False)
def load_data():
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        df = pd.DataFrame(data['data'])
        df['time'] = pd.to_datetime(df['last_updated'])
        df.set_index('time', inplace=True)
        df = df.resample('H').mean()
        return df
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

# Get data
data = load_data()

# Create a subheader
st.subheader('Historical Bitcoin price')

# Show the data as a chart
st.line_chart(data)

# Creating function for model
def train_model(data):
    X = data.index.values.reshape(-1, 1)
    y = data.values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    prediction = model.predict(X_test)
    mse = mean_squared_error(y_test, prediction)

    return model, mse

# Train model
model, mse = train_model(data)

# Show model performance
st.subheader('Model performance')
st.write('Mean Squared Error of the model is: ', mse)

# Show predictions on data
st.subheader('Forecast on test data')
plt.plot(data.index[-len(y_test):], y_test, label='Actual')
plt.plot(data.index[-len(y_test):], model.predict(X_test), label='Predicted')
plt.legend(loc='upper left')
st.pyplot()
