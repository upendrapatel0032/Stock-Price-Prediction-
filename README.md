# Stock-Price-Prediction using LSTM

<h2> Required Modules </h2>

* Steamlit
* Tensorflow
* Keras
* Numpy
* Pandas
* Matplotlib
* Yahoo Finance
* pandas_datareader
* scikit-learn

<h2> In a Nutshell </h2>

The project is made on Jupyter Notebook and VS Code. 

The prediction is done on closing prices from the data acquired through the python's yfinance module that allows the user to collect stock information of companies without any cost. 

The data is from 01/2010 to 12/2022. It is divided into 70% training and 30% testing data set. 

The model is trained on 100 steps to predict the value of 101st day. 

Feature scaling is done using MinMaxScaler from sklearn.preprocessing with feature range of ( 0 , 1 )

The model type is Sequential. The layer type is LSTM.

The model is compiled with Adam optimizer with loss set to Mean Squared Error (MSE). 
The model is fit with 50 epochs.

After model completion, test data is prepared and predictions are made. After scaling up the result, Original Vs Predicted Price graph is plotted using Matplotlib.pyplot. 

For showing our project to the others, we decide to use Streamlit that is a Python's open source framework and made a Web App from it. 

<h2> How to run the Web App ? </h2>

The code for the streamlit web app is stored in ***Web App.py***

After ensuring that all the libraries are installed in your VS Code, navigate to Run and Debug in the side panel and click on 'Start Debugging' with Python Module. It should open a streamlit web application in your default browser. 

<h2> How to use it ? </h2>

Enter the desired company's stock ticker in the input box of web app. The default is set to be 'AAPL'. 
You should see the data and graph changing corresponding to the stock ticker entered. 

<h2> Disclaimer </h2>

The project is strictly for educational purposes and real money betting should not be risked. 
