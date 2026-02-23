import streamlit as st
st.title("Welcome to basic streamlit app")
age =st.slider("Select your age",1,100)
city=st.selectbox("Select your city",["Delhi","Nashik","Pune"])
if st.button("show"):
    st.write("age",age)
    st.write("city",city)