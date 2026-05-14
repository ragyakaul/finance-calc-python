import streamlit as st


st.title('Finance Calculator')


st.logo("No.png", size="large")

st.caption("if you have time, you don’t have to race. You don’t need to nervously check stock prices every day. You don’t have financial pressure. You don’t need the stock market to “do something”. You don’t get suckered into get-rich-quick schemes. You don’t freak out when the market crashes. You can make time work for you. -Scott Pape, BareFoot Investor" )



with st.form('financecalc'):
    mortgageLeft = st.number_input('Mortgage left')
    interestRate = st.number_input('Interest Rate')
    monthlyRepayment = st.number_input('Monthly Repayment')
    savings = st.number_input('Savings')
    submit = st.form_submit_button('Submit')

    