import streamlit as st

st.title("Basic Form")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
dob = st.date_input("Date of Birth")

if st.button("Submit"):
    st.write("Registration Successful")
    st.write("First Name:", first_name)
    st.write("Last Name:", last_name)
    st.write("DOB:", dob)