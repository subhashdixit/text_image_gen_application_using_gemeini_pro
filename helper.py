from dotenv import load_dotenv
import os
import google.generativeai as genai
import textwrap
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

load_dotenv()  # take environment variables from .env.

# Configure the Generative AI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response_text(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

def get_gemini_response_image(input_text, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

def get_gemini_response(question):
    # Load Gemini Pro model
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat(history=[])

    response = chat.send_message(question, stream=True)
    return response