import streamlit as st
from PIL import Image
from helper import get_gemini_response_text, get_gemini_response_image, get_gemini_response

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Application")

# Sidebar with options
option = st.sidebar.radio("Select Option", ["Text Input", "Image Input", "Gemini chatbot"])

st.header("Gemini Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Text input option
if option == "Text Input":
    input_text = st.text_input("Input: ", key="input_text")
    submit_text = st.button("Ask the question")

    if submit_text and input_text:
        response = get_gemini_response_text(input_text)
        st.subheader("The Response is")
        st.write(response)  # Display response directly

# Image input option
elif option == "Image Input":
    st.subheader("Upload an image or enter text:")
    
    # Text input alongside image upload
    input_text = st.text_input("Input: ", key="input_text_image")
    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit_image = st.button("Submit")

    if submit_image:
        if uploaded_file:
            response = get_gemini_response_image(input_text,image)  # Pass image to function
            st.subheader("The Response is")
            st.write(response)  # Display response directly

# Gemini chatbot option
elif option == "Gemini chatbot":
    input_llm = st.text_input("Input: ", key="input_llm")
    submit_llm = st.button("Ask the question")

    if submit_llm and input_llm:
        response_llm = get_gemini_response(input_llm)
        st.subheader("The Response is")
        for chunk in response_llm:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("You", input_llm))
            st.session_state['chat_history'].append(("Bot", chunk.text))

    # Display chat history
    st.subheader("The Chat History is")
    for role, text in st.session_state.get('chat_history', []):
        st.write(f"{role}: {text}")


