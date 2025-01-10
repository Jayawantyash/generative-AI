import streamlit as st #ignore
import os
import textwrap


from IPython.display import display
from IPython.display import Markdown
#from altair.vegalite.v4.api import Chart

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


os.environ['GEMINI_API_KEY'] = ''

import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content('what is the speed of light')
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("yashBOT Application")

input=st.text_input("Input: ",key="input")


submit=st.button("I can help on your question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
