#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Description: stock market dashboard to show some charts and data

# Import the libraries

import streamlit as st
import pandas as pd
from PIL import Image


# In[3]:


st.write("""
# Stock Market Web Application -- Inputs Sample Test
Visually show data on a stock (Only MSFT)  Date range from Aug 3, 2009 - Aug 1, 2019
""")

image = Image.open("C:/Users/gregr/OneDrive/Pictures/tbot.PNG")
st.image(image, use_column_width=True)


# In[5]:


# Create a sidebar header

st.sidebar.header('User Input')

# Create a function to get the users input

def get_input():
    start_date = st.sidebar.text_input("Start Date", "8/03/2009")
    end_date = st.sidebar.text_input("End Date", "8/01/2019")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol

# Create a function to get the company name

def get_company_name(symbol):
    if symbol == "AMZN":
        return "Amazon"
    elif symbol == "TSLA":
        return "Tesla"
    elif symbol == "GOOG":
        return "Alphabet"
    elif symbol == "MSFT":
        return "Microsoft"
    else:
        "None"
        
# Create a function to get the proper company data and the proper timeframe from the user start date to the user end date

def get_data(symbol, start, end):
    
    # Load the data -------> This is where you would get alpacas data
    if symbol.upper() == 'MSFT':
        df = pd.read_csv("C:/Users/gregr/Documents/u-tor-fintech/03-Class-Activities/04-Pandas/4.2-Pandas-Review-Day/13-Portfolio-Returns/Resources/MSFT.csv", index_col="date", parse_dates=True, infer_datetime_format=True)

    else:
        df = pd.DataFrame(columns = ['Date', 'Close', 'Open', 'High', 'Low', 'Volume'])
        
    # Get the date range

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    
    # Set the start and end index rows both to 0
    start_row = 0
    end_row = 0
    
    # Start the dtae from the top data set and go down to see the users start date is less than or equal to the date in the dataset

    for i in range(0, len(df)):
        if start <= pd.to_datetime(df("Date")[i]):
            start_row = i
            break
    # Start from the bottom of the dataset and look up to see if users end date is greater than or equal to the date in the dataset
    for j in range (0, len(df)):
        if end >= pd.to_datetime(df["Date"][len(df)-l-j]):
            end_row = len(df) - 1 - j
            break
    
    #Set the index to the date
    df = df.set_index(pd.to_datetime(df["Date"].values))
    
    return df.iloc[start_row:end_row+1, :]

# Get users input

start, end, symbol = get_input()

# Get the data

df = get_data(symbol, start, end)

# Get the company name

company_name  = get_company_name(symbol.upper())

# Display the close price
st.header(company_name + " Close Price\n")
st.line_chart(df["Close"])

# Display the volume
st.header(company_name + " Close Price\n")
st.line_chart(df["Volume"])

# Get some stattistics on the data 
st.header('Data Statistics')
st.write(df.describe())


# In[ ]:




