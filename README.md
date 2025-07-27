
# AI Mood Companion (Offline)

A friendly AI chatbot that runs locally using Hugging Face models. No OpenAI key or internet billing needed.

## 💻 How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the app:
```
streamlit run ai_mood_companion_local.py
```

## 🔧 Features

- 💬 Understands user emotion from input text
- 🎯 Detects mood: **happy**, **sad**, **very sad**, or **neutral**
- 🧠 Uses **Prompt Engineering** to create real-time responses
- 🧱 Built with Hugging Face’s `DialoGPT-medium`
- 🖥️ Runs locally using **Streamlit UI**
- 🔒 Fully private (no cloud calls)

- 
## 🛠️ Tech Stack

- `Python`
- `Hugging Face Transformers` (`DialoGPT`)
- `TextBlob` (for sentiment analysis)
- `Streamlit` (for interface)
- `PyTorch`

  ## 🧠 How It Works

1. User enters their thoughts
2. Sentiment is analyzed (polarity)
3. A system-level prompt is crafted using Prompt Engineering
4. DialoGPT generates a personalized, friendly reply

---
## 📸 Screenshot
<img width="1913" height="853" alt="Screenshot 2025-07-28 005108" src="https://github.com/user-attachments/assets/a35f4d75-b39c-4cf1-838d-703e57407d26" />



