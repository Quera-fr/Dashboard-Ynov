import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            columns1, columns2 = st.columns(2)
            with columns1:
                st.image(message["content"][1])
            with columns2:
                st.subheader(message["content"][0])
                st.link_button("Go to gallery", message["content"][2])
        else:
            st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    rsp = requests.get(f'https://www.blogdumoderateur.com/?s={prompt}')
    soup = BeautifulSoup(rsp.text)

    titre = soup.find('article').find('h3').text
    img = soup.find('article').find('img')['src']
    link = soup.find('article').find('a').attrs["href"]

    response = f"<h1>{titre}</h1>"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        col1, col2 = st.columns(2)
        with col1:  
            st.subheader(titre)
        with col2:
            st.image(img)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": (titre, img, link)})