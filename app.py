import streamlit as st
from chain import translate

# Title of the web app
st.title("Language Translation App")


# Taking two integer inputs from the user
lang1 = st.text_input("Enter Language From:", "English")
lang2 = st.text_input("Enter Language To:", "Hindi")

# Text input to capture the user's name
content = st.text_input("What do you wish to translate?")

# Display the sum of the two numbers
if st.button("Translate"):
    output = translate(lang1, lang2, content)
    st.write(output['response'])

    # ## Use custom HTML with CSS to display the text in a smaller font
    st.markdown(
        f"""
        <style>
        .small-font {{
            font-size:6px;
            color: #555555;
        }}
        </style>
        
        <div class="small-font">
            <p><strong>Input Tokens:</strong> {output["input_tokens"]}</p>
            <p><strong>Output Tokens:</strong> {output["output_tokens"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

