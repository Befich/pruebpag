import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("""Salud mental en trabajo remoto""")
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #9c9c9c;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    "## This is the sidebar"

st.subheader('alo?')
