import streamlit as st

st.title("🎬 Movie Recommender")
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello {name}!")