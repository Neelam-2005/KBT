import streamlit as st
st.title("Simple Chatbot")
Question=st.text_input("Ask me Anything")
if st.button("Send"):
    st.write("question",Question)
    st.write("Reply Soon")