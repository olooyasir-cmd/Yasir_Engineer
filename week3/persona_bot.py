"""
Week 3 · Lab 3.2 — Give It a Personality
========================================
90% of a bot's personality lives in its SYSTEM PROMPT.
Here you build a live control panel for it.

Run it with:   streamlit run week3/persona_bot.py
"""

import streamlit as st
from openai import OpenAI

client = OpenAI()

# TODO: build a PERSONAS dictionary — name -> system prompt
PERSONAS = {
    # "Efua the Study Buddy": "You are Efua, a warm Ghanaian tutor...",
}

# ── THE CONTROL PANEL ────────────────────────────────────
with st.sidebar:
    st.header("🎛️ Control Panel")
    # TODO: selectbox to pick a persona
    # TODO: radio for tone (Friendly / Professional / Funny)
    # TODO: slider for creativity (temperature, 0.0 to 1.0)

# TODO: build the system_prompt from the choices above
# TODO: build conversation = [system message] + st.session_state.messages
# TODO: the chat loop (same as chatbot.py), but pass temperature too
