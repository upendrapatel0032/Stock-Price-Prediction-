import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
yf.pdr_override()
import tensorflow as tf 
from tensorflow import keras
import json

import streamlit as st




start = '2010-01-01'
end = '2022-12-31'

st.title('Stock Trend Predcition')

user_input = st.text_input('Enter Stock Ticker','AAPL')
df = pdr.get_data_yahoo(user_input, start, end )

#Describing Data

st.subheader('Data from 2010 - 2022')
st.write(df.describe())

#Visualization

st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize =(12,6))
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time Chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize =(12,6))
plt.plot(df.Close,label='Closing Price')
plt.plot(ma100,label='Moving 100 Average')
plt.legend()
st.pyplot(fig)


st.subheader('Closing Price vs Time Chart with 100MA & 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize =(12,6))
plt.plot(df.Close,label='Closing Price')
plt.plot(ma100,label='Moving 100 Average')
plt.plot(ma200,label='Moving 200 Average')
plt.legend()

st.pyplot(fig)

#Spliting data into training and testing

data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing =  pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

from sklearn.preprocessing import MinMaxScaler  #data scaling = reduces the difference                                            
# between the points in the data which results in greater accuracy. It comes under Data Preproccesing


scaler = MinMaxScaler(feature_range=(0,1))

data_training_array = scaler.fit_transform(data_training)


#Load My model

model = keras.models.load_model('keras_model4.keras')

#Testing Part
past_100_days = data_training.tail(100) 
final_df = pd.concat((past_100_days, data_testing),ignore_index = True,axis=0)

input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100: i])
    y_test.append(input_data[i,0])
    
x_test , y_test = np.array(x_test), np.array(y_test)
  
y_predicted = model.predict(x_test)
    
scaler = scaler.scale_ 
scale_factor = 1/scaler[0]
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor

#Final Graph
st.subheader('Predictions vs Original')
fig2 = plt.figure(figsize=(12,6))
plt.plot(y_test, 'b', label = "Original Price")
plt.plot(y_predicted, 'r', label = "Predicted Price")
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)
