import streamlit as st
import pandas as pd

# Upload file
uploaded_file = st.file_uploader("Choose a file", type="csv")
if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file, delimiter=';')

    # SELECT COLUNS
    selected_columns = st.multiselect("Sélectionnez les colonnes du dataframe",
                                      df.columns)
    
    # Data editor
    edited_df = st.data_editor(df[selected_columns])

    # Download button
    st.download_button(
        label="Download data as CSV",
        data=edited_df.to_csv(),
        file_name="large_df.csv",
        mime="text/csv",
    )