import sys
sys.path.append("..")

import os
import json
import time
import pandas as pd
import streamlit as st
# from streamlit_extras.mention import mention
# import chromadb
from openai import OpenAI
import json
import yaml
from utils import *

# Access your secret
api_key = os.getenv("API_KEY")
# chat_api_key = os.getenv("sambanova_API_KEY")

#############################################################################################################
#############################################################################################################

# Initialize the app
# def init():
#     global K

#     st.set_page_config(
#         page_title="Grievance Registration Assistant",
#         page_icon="🧺",
#         layout="centered",
#         initial_sidebar_state="expanded",
#     )

#     with st.sidebar:
#         option = st.selectbox(
#             "Please select the preferred language",
#             ["English", "Hindi"],
#             index=0,
#             placeholder="Select prefered language...",
#         )
        
#     st.header('Grievance Registration Assistant (GRA)',divider=True)



def main():

    global K

    st.set_page_config(
        page_title="Grievance Registration Assistant",
        page_icon="🧺",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    with st.sidebar:
        st.session_state.option = st.selectbox(
            "Please select the preferred language",
            ["English", "Hindi"],
            index=0,
            placeholder="Select prefered language...",
        )

    # Initialize chat history
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role": "system", "content": get_systemPrompt()}
                ]
        
    if st.session_state.option == "English":
        st.header('Grievance Registration Assistant (GRA)',divider=True)

        if prompt:=st.chat_input("Say something"): # Prompt for user input and save to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

        for message in st.session_state.messages[1:]: # Display the prior chat messages
            with st.chat_message(message["role"]):
                st.write(message["content"], unsafe_allow_html=False)
        
        # If last message is not from assistant, generate a new response
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    start_time = time.time()
                    response = generate_response(st.session_state.messages)
                    end_time = time.time()
                    st.toast(f'Response generated in :green[{end_time - start_time:.2f}] seconds', icon='✅')
        
                    message = {"role": "assistant", "content": response}
                    st.session_state.messages.append(message) # Add response to message history
                st.write(response, unsafe_allow_html=False)
    
    if st.session_state.option == "Hindi":
        st.header('शिकायत पंजीकरण सहायक (जी.आर.ए.)',divider=True)

        if prompt:=st.chat_input("Say something"): # Prompt for user input and save to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

        for message in st.session_state.messages[1:]: # Display the prior chat messages
            with st.chat_message(message["role"]):
                st.write(translate_ENG_to_HIN(message["content"]), unsafe_allow_html=False)
        
        # If last message is not from assistant, generate a new response
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    start_time = time.time()
                    response = generate_response(st.session_state.messages)
                    end_time = time.time()
                    st.toast(f'Response generated in :green[{end_time - start_time:.2f}] seconds', icon='✅')
        
                    message = {"role": "assistant", "content": response}
                    st.session_state.messages.append(message) # Add response to message history
                st.write(translate_ENG_to_HIN(response), unsafe_allow_html=False)
            
if __name__ == "__main__":
    main()