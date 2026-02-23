import streamlit as st

st.markdown("""
<style>
.stButton > button {
    background-color: green;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

st.title("Welcome to basic streamlit app")

age = st.slider("Select your age", 1, 100)
city = st.selectbox("Select your city", ["Delhi", "Nashik", "Pune"])

if st.button("Show"):
    st.write("Age:", age)
    st.write("City:", city)