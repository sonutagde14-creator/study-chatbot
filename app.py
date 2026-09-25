
import streamlit as st

st.set_page_config(page_title="Study Buddy - AI Chatbot", layout="wide")

with st.sidebar:
    st.markdown("### About")
    st.write("Study Buddy uses a hybrid approach:")
    st.write("1. Language KB — keyword matching")
    st.write("2. General CS KB — fallback dataset")
    st.write("3. AI fallback — for outside questions")
    st.markdown("---")
    st.success("General CS: 33 pairs")

st.title("📚 Study Buddy — AI Chatbot")
st.write("Ask questions about Computer Science. Made by Sonu Tagde")

topic = st.selectbox("Select topic / language:", ["General CS", "Python", "Java", "DBMS"])
st.markdown(f"## Active topic: {topic}")
st.markdown("---")

st.markdown(f"Hi! I'm Study Buddy — focused on {topic} 🤖")

question = st.text_input(f"Ask a {topic} question...")

if question:
    if "python" in question.lower():
        st.success("Python ek easy programming language hai!")
    elif "java" in question.lower():
        st.success("Java Object Oriented Language hai!")
    elif "loop" in question.lower():
        st.success("Loop repeat karne ke liye use hota hai!")
    else:
        st.info(f"Aapne pucha: {question} | Iska jawab mai sikh raha hu!")
