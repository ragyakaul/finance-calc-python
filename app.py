import streamlit as st
import pandas as pd # to experiment with charts - we will need this for ficalc
import numpy as np
import values as values
from main import monthlyInterestCharged, monthlyPrincipalSaved, savingsTowardsStocks, savingsTowardsMortgage

st.title('Finance Calculator')


st.logo("No.png", size="large")

st.caption("if you have time, you don’t have to race. You don’t need to nervously check stock prices every day. You don’t have financial pressure. You don’t need the stock market to “do something”. You don’t get suckered into get-rich-quick schemes. You don’t freak out when the market crashes. You can make time work for you. -Scott Pape, BareFoot Investor" )



with st.form('financecalc'):
    mortgageLeft = st.number_input('Mortgage left', min_value=0, value=values.mortgageLeft)
    interestRate = st.number_input('Interest Rate', min_value=0.0, value=values.interestRate)
    monthlyRepayment = st.number_input('Monthly Repayment', value=values.monthlyRepayment)
    savings = st.number_input('Savings', value=values.savings)
    submit = st.form_submit_button('Submit')



monthlyInterest = monthlyInterestCharged(mortgageLeft, interestRate)
st.write(f"Monthly interest: {monthlyInterest} aka a rent of {monthlyInterest/4} per week")

monthlyPrincipal = monthlyPrincipalSaved(monthlyRepayment, monthlyInterest)
st.write(f"Monthly Principal: {monthlyPrincipal}")

monthlyStocksSavings = savingsTowardsStocks(savings, monthlyPrincipal)
st.write(f"Monthly Stock Savings: {monthlyStocksSavings}")

monthlyExtraMortgageContribution = savingsTowardsMortgage(savings, monthlyStocksSavings)
st.write(f"Monthly Extra Mortgage Contribution: {monthlyExtraMortgageContribution}")

### Put some sort of 'Update' button that will modify values you care about for next time 
### Like, it'll update the mortgage with what you ACTUALLY put in, along with the stocks
### For the next part, the graphs need to reflect actual contribution, that means
### Make a graph that shows 'if you pay this towards mortgage, here's when your mortgage is paid of & the rate etc'
### IF you put this towards stocks, here's how your stocks scale

st.write("## Graph example")

# This data will be returned by your backend functions and processed by streamlit
chart_data = pd.DataFrame( 
    np.random.randn(20, 3),
    columns = ["a", "b", "c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)