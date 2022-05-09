"""
Class: CS230--Section 3
Name: Will Gao
Description: Final Project
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""


import streamlit as st
from apps import Home, Data, Visualizations

st.set_page_config(page_title="UFO Data", page_icon=":alien", layout="wide")

PAGES = {
    "Home": Home,
    "Data": Data,
    "Visualizations": Visualizations
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

