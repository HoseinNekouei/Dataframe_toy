import streamlit as st
import pandas as pd

file_path= '/home/hossein/Documents/chatbot_project/twitter_train_corpus.csv'
df = pd.read_csv(file_path, nrows=1000)

# Get Query through input box
user_input= st.text_input('input your query...')

#Only access to your df
query = eval(user_input, {'__builtins__':{}}, {'df': df})

if not query.empty:
    st.write(query)
else:
    st.write(df)

