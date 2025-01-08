import streamlit as st
import yfinance as yf
import datetime


st.title("Stock Price Analyser")
stock_name = st.text_input("which stock do you want to analyse","MSFT")

ticker_data=yf.Ticker(stock_name)
start_date=st.date_input("Please enter Starting Date",datetime.date(2023,12,1))
end_date=st.date_input("Please enter Ending Date",datetime.date(2024,12,1))

ticker_df =ticker_data.history(period='1d',start=start_date,end=end_date)

print(ticker_df)
st.dataframe(ticker_df)

st.subheader("Here is the raw daywise stock price")
st.dataframe(ticker_df.head())

st.subheader(body="Price movement over time")
st.line_chart(ticker_df['Close'])

st.subheader("Volume over time")
st.line_chart(ticker_df['Volume'])