import streamlit as st
import pandas as pd
import seaborn as sns


# Configuration de la page
st.set_page_config(
    page_title="Data Processing",
    page_icon="👋",
    layout="wide", # wide
)

st.title('Data Processing')


# Upload file
uploaded_file = st.file_uploader("Choose a file", type="csv")



if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file, delimiter=';')

    if st.sidebar.checkbox('Data Editor'):

       

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

    if st.sidebar.checkbox("Afficher les Graphiques"):

        graph_type = st.sidebar.selectbox("Sélectionnez un type de graphique",
                        ['Histogramme', 'Scatter Plot', 'Pie Chart', "Box Plot"])

        
        columns = st.sidebar.selectbox("Sélectionnez les collonnes", 
                         df.columns)
        
        if graph_type == 'Histogramme':
            st.pyplot(sns.histplot(df[columns]).figure)
        
        if graph_type == 'Box Plot':
            try:
                st.pyplot(sns.boxplot(x=df[columns]).figure)
            except:
                st.error('Sélectionnez une colonne numérique')