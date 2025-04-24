import streamlit as st
import pandas as pd

file_path= '/home/hossein/Documents/chatbot_project/twitter_train_corpus.csv'
df = pd.read_csv(file_path, nrows=1000)

# Get Query through input box
user_input= st.text_input('Enter your pandas query using "df", e.g., df[df["label"] == "positive"]')

query_result = None

if user_input:
    try:
        # Only safe access to df
        query_result = eval(user_input, {'__builtins__': {}}, {'df': df})
        
        if isinstance(query_result, pd.DataFrame) and not query_result.empty:
            st.write(query_result)
        else:
            st.warning("Query executed but returned no results.")
    except Exception as e:
        st.error(f"Error in query: {e}")
        st.write("Showing full dataset below:")
        st.write(df)
else:
    st.write("Awaiting query input. Showing full dataset below:")
    st.write(df)
