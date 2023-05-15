import streamlit as st
import pandas as pd

def load_data_dun():
    df = pd.read_csv('data/prn_result_dun.csv')
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    return df

df_dun = load_data_dun()

# Calculate total wins by state and abbreviation
count_wins = df_dun[df_dun['STATUS'] == 'MENANG'].pivot_table(index='NEGERI', columns='PARTI', values='STATUS', aggfunc='count', fill_value=0)

# Calculate total wins for each abbreviation across all states
total_wins = count_wins.sum().astype(int)

# Add a row for total wins for all states for each abbreviation
total_win = count_wins.append(total_wins.rename('TOTAL'))

# Display the results in a table on Streamlit
st.write("Total Wins by State and Abbreviation")
st.dataframe(total_win, use_container_width=True)



