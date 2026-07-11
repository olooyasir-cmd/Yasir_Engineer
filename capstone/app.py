"""
🎓 MY CAPSTONE APP
==================
This is mine. My idea, my code, my deployed app.

Run it with:   streamlit run capstone/app.py
"""

import streamlit as st
from openai import OpenAI

client = OpenAI()

SYSTEM = "You are ..."   # TODO: my system prompt

st.title("My Capstone App")

# TODO: build the smallest working version FIRST:
#       input -> AI call -> show the answer
#
# Then add features one at a time, testing after each.
