import streamlit as st
import requests

# st.title("My Personal RAG Assistant")

# question = st.text_input("Ask a question about my CV")

# if st.button("Ask"):
#     res = requests.post(
#         "http://127.0.0.1:8000/query",
#         json={"question": question}
#     )
#     st.write(res.json()["answer"])


# streamlit run app.py
#dont run it in command prompt
#streamlit run c:/Users/USER/Desktop/RAG/streamlit/str_app.py

import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Personal RAG Assistant", layout="centered")

# Title & description
st.title("My Personal RAG Assistant")
st.write("Ask questions about my CV and personal documents.")

st.markdown(
    """
    **Assistant Persona:**  
    I answer questions strictly based on my personal documents  
    (CV, experience, education, projects).
    """
)


# Input box
question = st.text_input("Ask a question")

# Button
if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = requests.post(
                "http://127.0.0.1:8000/query",
                json={"question": question}
            )

        if response.status_code == 200:
            data = response.json()

            st.subheader("Answer")
            st.write(data["answer"])
        else:
            st.error("Something went wrong. Please try again.")
