import streamlit as st
import pandas as pd
import time
import numpy as np

st.title('Welcome to T.Bot')
st.write("Please enter your information in the side bar" )
st.write("Your Personal Infomation")

age = [18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70]
investment_term = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
international_diversification = ["Yes", "No"]
retirement_age = 65

name = st.sidebar.text_input('Your Name', '')
st.write('Your name:', name)


age_option = st.sidebar.selectbox(
'Your age:',
age)
'Your age: ', age_option

inv_term_option = st.sidebar.selectbox(
'Your investment horizon (years):',
investment_term)
'Your investment horizone (years): ', inv_term_option

int_div_option = st.sidebar.selectbox(
'Do you want to invest outside the US?',
international_diversification)
'International Divesification?: ', int_div_option

initial_investment = st.sidebar.text_input('Initial Investment (US$)', '10,000')
st.write('Initial investment amount (US$):', initial_investment)

#Determine Risk Tolerance
risk_tolerance = 0
if age_option <60:
    if inv_term_option < 2:
        risk_tolerance = risk_tolerance+1
    elif inv_term_option < 4:
        risk_tolerance = risk_tolerance+2
    elif inv_term_option < 6:    
        risk_tolerance = risk_tolerance+3
    elif inv_term_option < 8:    
        risk_tolerance = risk_tolerance+4
    elif inv_term_option > 7:    
        risk_tolerance = risk_tolerance+5
else: risk_tolerance = risk_tolerance+1

    
st.write('Your investment risk tolerance level:', risk_tolerance)       


#Determine Optimal Investment Portfolio

portfolios = {
    1: {"etf":"AOK", "name": "Core Conservative Allocation"},
    2: {"etf":"AOM", "name": "Core Moderate Allocation"},
    3: {"etf":"AOR", "name": "Core Growth Allocation"},
    4: {"etf":"AOA", "name": "Core Aggressive Allocation"},
    5: {"etf":"IVV", "name": "Core S&P 500"},
    }

if risk_tolerance == 1:
    st.write('Your optimal investment portfolio:', portfolios[1]["name"])
elif risk_tolerance == 2:    
    st.write('Your optimal investment portfolio:', portfolios[2]["name"])
elif risk_tolerance == 3:    
    st.write('Your optimal investment portfolio:', portfolios[3]["name"])
elif risk_tolerance == 4:    
    st.write('Your optimal investment portfolio:', portfolios[4]["name"])
else: st.write('Your optimal investment portfolio:', portfolios[5]["name"])  




