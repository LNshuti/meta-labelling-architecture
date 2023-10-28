import pandas as pd
from openbb_terminal.sdk import openbb
import streamlit as st
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics 
import warnings 
warnings.filterwarnings('ignore')

# Create load_data function that takes a list of crypto tokens as inputs and returns a dataframe of historical prices
@st.cache_data
def load_data():
    # Load data using openbb.crypto.load 
    btc_df = openbb.crypto.load(symbol="btc",to_symbol="usd",start_date="2019-01-01",source="YahooFinance")
    eth_df = openbb.crypto.load(symbol="eth",to_symbol="usd",start_date="2019-01-01",source="YahooFinance")
    xrp_df= openbb.crypto.load(symbol='xrp', to_symbol='usd', start_date='2019-01-01', source="YahooFinance")
    # Combine btc and eth dataframes and save under /data. Append current date to the filename. 
    # Add a new column identifying which coin the row belongs to. 
    btc_df['coin'] = 'btc'
    eth_df['coin'] = 'eth'
    xrp_df['coin']= 'xrp'
    btc_eth_xrp_df = pd.concat([btc_df,eth_df,xrp_df],axis=0)

    return btc_eth_xrp_df


# Create a simple function feature_engineering that takes a dataframe of historical prices as input and returns a dataframe with engineered features
def feature_engineering(df):
    df = df.reset_index()
    df['date'] = df['date'].astype(str)  # Convert the column to a string
    splitted= df.date.str.split('-', expand=True)
    df['year']= splitted[0].astype('int')
    df['month']= splitted[1].astype('int')
    df['day']= splitted[2].astype('int')
    df['is_quarter_end']= np.where(df['month']%3==0,1,0)

    df['open-close']= df['Open']- df['Close']
    df['low-high']= df['Low']- df['High']
    df['target']= np.where(df['Close'].shift(-1) > df.Close, 1, 0)

    return df

# Create train_model function that takes a dataframe of historical prices as input and returns a trained model and MSE

def train_model(df):
    features= df[['open-close', 'low-high', 'is_quarter_end']]
    target= df['target']

    scaler= StandardScaler()
    features= scaler.fit_transform(features)

    X_train, X_valid, Y_train, Y_valid= train_test_split(features, target, test_size=0.1, random_state=202)

    # Fit a logistic regression model to the data
    model= LogisticRegression()
    model.fit(X_train, Y_train)

    # Predict the validation set
    Y_pred= model.predict(X_valid)

    # Calculate the MSE
    mse= metrics.mean_squared_error(Y_valid, Y_pred)

    return model, mse


# Run the load_data and train_model functions
# Show the outputs as a streamlit application 

def main():

    df_crypto= load_data()

    df_crypto_features = feature_engineering(df_crypto)

    model, mse= train_model(df_crypto_features)

    st.title('Crypto Price Prediction')
    st.write('This application predicts the price of crypto currencies.')
    st.write('Raw data')
    st.write(df_crypto.tail())

    st.write('Feature engineered data')
    st.write(df_crypto_features.tail())


    st.sidebar.title('User Input Features')
    st.sidebar.write('Select the crypto currency and the date.')

    # Create sidebar inputs for user to select crypto currency and date
    # Create a button to run the model and display the results

    coin= st.sidebar.selectbox('Coin', df_crypto['coin'].unique())
    date= st.sidebar.date_input('Date')
    submit= st.sidebar.button('Predict')

    if submit: 
        st.write('The predicted price is: ', model.predict([[0.1, 0.2, 0]]))
        st.write('The MSE is: ', mse)

if __name__ == '__main__':
    main()



