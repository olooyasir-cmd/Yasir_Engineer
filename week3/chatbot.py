"""
Week 3 · Lab 3.1 — A Chatbot That Remembers  ⭐ THE FLAGSHIP
===========================================================
The big idea: "memory" is just a growing list of messages
that you re-send to the AI every single turn.

Run it with:   streamlit run week3/chatbot.py
"""

import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("🤖 My Chatbot")

# ── 1. THE MEMORY BOX ────────────────────────────────────
# TODO: create st.session_state.messages ONCE (use the "if not in" guard)
#       Seed it with a system message to give your bot a persona.


# ── 2. REPLAY THE HISTORY ────────────────────────────────
# TODO: loop over st.session_state.messages and show each one
#       as a chat bubble. (Skip the "system" message!)


# ── 3. CAPTURE NEW INPUT ─────────────────────────────────
# TODO: prompt = st.chat_input(...)
#       If there's a prompt: save it, show it.


# ── 4. GET THE AI REPLY (with full context!) ─────────────
# TODO: send st.session_state.messages (the WHOLE list) to the AI,
#       show the answer, then save it back to the list.
