"""
Week 4 · Lab 4.2 — The Auto-Analyst Dashboard
=============================================
Upload data -> get KPIs, an AI-written summary, AND a chart.
No questions needed. This is the most product-like app you build.

Run it with:   streamlit run week4/dashboard.py
"""

import streamlit as st
import pandas as pd
from openai import OpenAI

client = OpenAI()

st.set_page_config(page_title="Auto-Analyst", page_icon="📊", layout="wide")
st.title("📊 Auto-Analyst Dashboard")

# TODO: file uploader

# ── 1. KPI CARDS ─────────────────────────────────────────
# TODO: find numeric columns with df.select_dtypes(include="number")
# TODO: show 3 metrics with st.columns(3) and st.metric(...)

# ── 2. FIND THE STORY ────────────────────────────────────
# TODO: groupby a text column, sum a number column, sort it

# ── 3. AI WRITES THE SUMMARY ─────────────────────────────
# TODO: send the grouped summary to the AI, ask for 3 bullet insights

# ── 4. AUTO-CHART ────────────────────────────────────────
# TODO: st.bar_chart(summary)
