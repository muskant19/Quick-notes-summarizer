# app.py
import streamlit as st
import nltk

# Ensure required NLTK resources are downloaded
nltk.download("punkt")
nltk.download("punkt_tab")
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

st.title("📝 Quick Notes Summarizer")
st.write("Paste your notes below and get a concise summary.")

# User input
notes = st.text_area("Enter your notes:")

if st.button("Summarize"):
    if notes.strip():
        parser = PlaintextParser.from_string(notes, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, 3)  # 3 sentences
        st.subheader("Summary:")
        for sentence in summary:
            st.write("-", sentence)
    else:
        st.warning("Please enter some text to summarize.")
