# app.py

import streamlit as st
from model import predict_message

# Page config
st.set_page_config(page_title="Spam Detector", page_icon="📧")

# UI
st.title("📧 Spam Email Detector")
st.markdown("Enter an email message to find out if it's **Spam** or **Ham**.")

email_text = st.text_area("✉️ Your Email Content", height=200, placeholder="Type or paste the email content here...")

if st.button("🔍 Check Spam"):
    if email_text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Analyzing..."):
            prediction = predict_message(email_text)
            color = "red" if prediction.lower() == "spam" else "green"

        st.markdown(f"<h3 style='color:{color};'>Prediction: {prediction}</h3>", unsafe_allow_html=True)
