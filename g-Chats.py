import streamlit as st
import google.generativeai as genai

# Update API key and configure the new model
genai.configure(api_key="AIzaSyDkygjsj_4ySmDAfNirvfiFQsnzvbdzodY")

# Function to load gemini-1.5-flash
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text, prompt):
    response = model.generate_content([input_text, prompt])
    return response.text

st.set_page_config(page_title="My_Chatbot")
# Add some custom CSS for styling
st.markdown(
    """
    <style>
    .st-emotion-cache-1r4qj8v {
        background-image: url('https://images.unsplash.com/photo-1490818387583-1baba5e638af?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');  /* Add your background image URL here */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: Arial, sans-serif;  /* Specify your preferred font family */
    }
    .st-emotion-cache-gh2jqd{
            width: 84%;
    margin-left: 32%;
    padding: 6rem 1rem 10rem;
    max-width: 46rem;
    }
    .header {
        color: #008080;
        text-align: center;
        font-size: 36px;
        margin-bottom: 20px;
    }
    .subheader {
        color: #696969;
        text-align: center;
        font-size: 24px;
        margin-bottom: 10px;
    }
    .button {
        background-color: #008080;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 18px;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .error-message {
        color: red;
        text-align: center;
        font-size: 18px;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("G-Chats")

# Text input for user to type ingredients
user_input = st.text_input("Type your query...")

submit = st.button("Go")

# Prompt for gemini
input_prompt = """
You are an intelligent and versatile assistant capable of understanding and responding to a wide range of tasks and queries.
Based on the user's input, provide clear and helpful information, guidance, or solutions. Ensure your responses are accurate, 
concise, and easy to understand, regardless of the topic or request.
"""


if submit:
    if not user_input:
        st.error("Please type a valid query")
    else:
        response = get_gemini_response(user_input, input_prompt)
        st.subheader("The response is")
        st.write(response)
