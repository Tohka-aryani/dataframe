import pandas as pd
import streamlit as st

# Load data into a pandas DataFrame
data = pd.read_csv("politiko 2/prn14_result_dun.csv")

# Group data by state and abbreviation, and calculate the sum of wins for each group
totals = data.groupby(["NEGERI", "PARTI"])["STATUS"].sum().reset_index()

# Display the results in a table on Streamlit
st.write("Total Wins by State and Abbreviation")
st.dataframe(totals)
