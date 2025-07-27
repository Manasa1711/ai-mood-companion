import streamlit as st
from textblob import TextBlob
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Set up Streamlit page
st.set_page_config(page_title="💖 AI Mood Companion", layout="centered")

# Load DialoGPT model
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
    return tokenizer, model

tokenizer, model = load_model()

# Detect emotion based on sentiment polarity
def detect_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity < -0.4:
        return "very sad"
    elif polarity < -0.2:
        return "sad"
    elif polarity > 0.5:
        return "happy"
    else:
        return "neutral"

# Generate AI response using DialoGPT with a system prompt
def generate_reply(user_input, chat_history_ids=None):
    # System-level prompt to guide the tone and intent
    system_prompt = (
        "You are a friendly and caring AI friend. If the user feels low, suggest positive thoughts, fun ideas, "
        "inspiring movies, or comforting words. Respond like a real friend.\n"
        f"User: {user_input}\nAI:"
    )

    input_ids = tokenizer.encode(system_prompt + tokenizer.eos_token, return_tensors="pt")
    bot_input_ids = input_ids if chat_history_ids is None else torch.cat([chat_history_ids, input_ids], dim=-1)

    output_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        temperature=0.8,
        top_k=50
    )
    reply = tokenizer.decode(output_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return reply, output_ids

# Streamlit UI
st.title("💖 AI Mood Companion (Offline)")
st.markdown("Your emotional buddy – no cloud needed. Just talk to me 💬")

# Session state for maintaining chat history
if "history" not in st.session_state:
    st.session_state.history = None

# User input
user_input = st.text_area("How are you feeling today?", height=150)

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking like a real friend..."):
            mood = detect_emotion(user_input)
            reply, st.session_state.history = generate_reply(user_input, st.session_state.history)

            st.markdown(f"### 🧠 Detected Mood: `{mood.upper()}`")
            st.markdown("### 💬 AI Friend Says:")
            st.success(reply)
    else:
        st.warning("Please write something before sending.")
