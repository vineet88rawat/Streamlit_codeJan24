import streamlit as st

st.title("Learning Streamlit")

st.header("My First App")
st.write("learning streamlit for the first time")

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")


genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)

st.write("You selected:", genre)