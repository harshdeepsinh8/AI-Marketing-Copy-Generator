import streamlit as st
from Chains import AIChain
from Utils import clean_text

# Initialize AI Model
ai_chain = AIChain()

# Streamlit UI
st.title("📢AI-Powered Marketing Copy Generator📢")

brand = st.text_input("Brand Name")
description = st.text_area("Product/Service Description")
audience = st.text_input("Target Audience (e.g., fitness enthusiasts, tech startups, eco-conscious consumers)")
tone = st.selectbox("Select Tone", ["Exciting", "Professional", "Casual"], index=0)

if st.button("Generate Copy"):
    with st.spinner("Generating marketing copy..."):
        marketing_copy = ai_chain.generate_marketing_copy(brand, description, audience, tone)
        st.subheader("Generated Marketing Copy:")
        st.write(marketing_copy)
