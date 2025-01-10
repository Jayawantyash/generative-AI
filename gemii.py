
import streamlit as st
import os
import textwrap
from PIL import Image



os.environ['GEMINI_API_KEY'] = ''


import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])


## Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('models/gemini-2.0-flash-thinking-exp-1219')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title=" Image CREATION ")

st.header("YASH AI IMAGE APP")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Explain me about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
