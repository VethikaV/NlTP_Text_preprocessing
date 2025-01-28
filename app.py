from dotenv import load_dotenv
import streamlit as st
import chain

load_dotenv()

def Code_Generator():
    """
    Code Generator Bot
    """
    with st.form("Code_Generator"):
        
        language = st.selectbox(
        "Select the programming language:",
        ["Python", "JavaScript", "Java", "C++", "Go", "Ruby"]
    )
        problem_statement = st.text_input("Enter the Problem Statement")
        submitted = st.form_submit_button("submit",type="primary")
        if(submitted):
            response =chain.Generate_code(language,problem_statement)
            st.info(response)

Code_Generator()