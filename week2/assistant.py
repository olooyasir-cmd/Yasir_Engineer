"""
Week 2 · Lab 2.1 — Market Assistant (CLI)
=========================================
Your code thinks for the first time. 🧠

Before running, make sure your API key is set as an environment variable:
    OPENAI_API_KEY

Run it with:   python week2/assistant.py
"""

from openai import OpenAI

client = OpenAI()   # automatically finds your OPENAI_API_KEY

# TODO: create a dictionary of your prices (your "price board")
prices = {}


def ask_assistant(question):
    """Send a question to the AI and return its answer."""
    # TODO: build your system prompt using the prices
    # TODO: call client.chat.completions.create(...)
    # TODO: return the reply text
    pass


if __name__ == "__main__":
    # TODO: ask the assistant a question and print the answer
    pass
