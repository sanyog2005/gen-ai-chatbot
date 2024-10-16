from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import base64
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="ai expert")

st.header("YOUR PERSONAL FITNESS AI ASSISTANT")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask any query related to health and fitness")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
    
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("HD-wallpaper-motivation-fitness-workout-dark-ultra-sports-fitness-dark-motivation-workout.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpapers.com/images/featured/barbell-am7v48yepmncv6c6.jpg");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 

background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("All progress takes place outside the comfort zone.")
st.sidebar.header("Fitness Expert")