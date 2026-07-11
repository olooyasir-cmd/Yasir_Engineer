"""
Week 4 · Lab 4.1 — Talk to a CSV
================================
The AI reads TEXT, not files. So: pandas reads the file,
you convert it to text, and hand it to the AI.

Run it with:   streamlit run week4/data_chat.py
"""

import streamlit as st
import pandas as pd
from openai import OpenAI

client = OpenAI()

st.title("📊 Talk to Your Data")

# TODO: uploaded = st.file_uploader("Upload a CSV", type="csv")

# TODO: if uploaded:
#         df = pd.read_csv(uploaded)
#         show the dataframe + row/column count

# TODO: add a question box

# TODO: convert the data with df.to_string() and send it to the AI
#       inside the prompt, then show the answer
