import streamlit as st
import pandas as pd
import seaborn as sns

# Configuration de la page
st.set_page_config(
    page_title="My Dashboard",
    page_icon="👋",
    layout="wide", # wide
)



@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/Quera-fr/Python-Programming/refs/heads/main/data.csv')


try :
    st.sidebar.write(st.secrets['API_KEY'])
except:
    st.sidebar.error('Absence de clé')

df = load_data()

# Title
st.title('My Dashboard - Kevin Duranty')

# Subtitle
st.subheader('Présentation de données')

# Champ de texte
name = st.text_input('Entrez votre nom')

st.write(f'Bonjour {name}')

# Text
st.write('Présentation de données avec Streamlit')

# Checkbox
if st.checkbox('Afficher le formulaire'):
    st.write(df)


# Image 
st.sidebar.image("https://cdn.cookielaw.org/logos/09f2ba89-076e-413b-b34f-a8d20370f3f5/35c98a5f-cba8-4b1a-959f-c5a7c260dfda/e0191cfb-2e2a-43c1-a11f-929eb86731a0/logo.png")

# Videp 
st.sidebar.video("https://www.youtube.com/watch?v=RKEKGxJ_WOQ")


# Formulaires
with st.form(key='my_form'):

    col1, col2 = st.columns(2)

    with col1:
        # Select Box
        profession = st.selectbox("Sélectionnez une profession", df.Profession.unique())

        # Slider
        age = st.slider("Selectionnez une tranche d'âge", 
                        df.Age.min(), df.Age.max(),     # Min, Max
                        (df.Age.min(), df.Age.max()))   # Default value
        
        button = st.form_submit_button(label='Valider')
            
    with col2:
        if button:
            data_age = df[(df.Profession == profession) &
                        (df.Age>age[0]) &
                        (df.Age<age[1])].Age
            
            plot = sns.histplot(data_age, bins=age[1]-age[0])
            st.pyplot(plot.figure)

        