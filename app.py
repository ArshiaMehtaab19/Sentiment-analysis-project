import streamlit as st
from nltk.sentiment.vader 
import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

# Page setup
st.set_page_config(page_title="Sentiment Analyzer", page_icon="💬", layout="centered")

# Custom styling
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            font-weight: bold;
            color: #4A90E2;
            text-align: center;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            font-size: 14px;
            color: gray;
        }
        .result-box {
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            padding: 16px;
            border-radius: 12px;
            color: #333333;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">💬 Sentiment Analysis with Emojis</div>', unsafe_allow_html=True)
st.markdown("Analyze your sentence and discover its sentiment — positive, negative, or neutral.")

# Input
user_input = st.text_area("✍️ Enter a sentence for analysis:", height=150)

# Button
if st.button("🔍 Analyze Sentiment"):
    if user_input.strip():
        scores = analyzer.polarity_scores(user_input)
        compound = scores['compound']

        # Logic
        if compound >= 0.05:
            sentiment = "Positive 😊"
            bg_color = "#D4EDDA"  # Light green
        elif compound <= -0.05:
            sentiment = "Negative 😞"
            bg_color = "#F8D7DA"  # Light red
        else:
            sentiment = "Neutral 😐"
            bg_color = "#FFF3CD"  # Light yellow

        # Output
        st.markdown(f"""
            <div class="result-box" style="background-color: {bg_color};">
                Sentiment: {sentiment}<br>
                Compound Score: {compound:.2f}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please enter a sentence to analyze.")

# Footer
st.markdown('<div class="footer">Made with ❤️</div>', unsafe_allow_html=True)
