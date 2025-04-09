# app.py

import streamlit as st
from model import predict_message

# Page config
st.set_page_config(page_title="SMS Spam Detector", page_icon="📩")

# UI
st.title("📩 SMS Spam Detector")
st.markdown("Enter an SMS message to find out if it's **Spam** or **Ham** (Not Spam).")

sms_text = st.text_area("📨 Enter your SMS message:", height=200, placeholder="Type or paste the SMS content here...")

if st.button("🔍 Detect Spam"):
    if sms_text.strip() == "":
        st.warning("Please enter a message to analyze.")
    else:
        with st.spinner("Analyzing message..."):
            prediction = predict_message(sms_text)
            color = "red" if prediction.lower() == "spam" else "green"

        st.markdown(f"<h3 style='color:{color};'>Prediction: {prediction}</h3>", unsafe_allow_html=True)
