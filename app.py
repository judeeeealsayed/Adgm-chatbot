import streamlit as st

st.set_page_config(
    page_title="ADGM Chatbot",
    layout="centered",
    initial_sidebar_state="auto",
)

# Custom CSS for white background and big centered logo
st.markdown(
    """
    <style>
        body {
            background-color: white;
        }
        .centered-logo {
            display: flex;
            justify-content: center;
            margin-bottom: 30px;
        }
        .centered-logo img {
            width: 50vw;  /* 50% of viewport width */
            height: auto;
            max-width: 600px;  /* max width so it doesn't get too big on large screens */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Centered logo with new styling
st.markdown('<div class="centered-logo">', unsafe_allow_html=True)
st.image("company_logo.png")
st.markdown('</div>', unsafe_allow_html=True)

st.title("Welcome to ADGM Chatbot")

st.write("🤖 Chatbot coming soon...")

user_input = st.text_input("Ask me anything:")

if user_input:
    st.write("This is a placeholder. Your question was:", user_input)
