# AI-Powered Marketing Copy Generator 🚀

## How It Works 🛠️

This Streamlit web app generates **personalized marketing copy** using **Groq Cloud's LLaMA model**. Users provide basic details about their brand, and the AI generates:

- **A catchy headline**
- **A short marketing description**
- **Three relevant hashtags**
- **A call-to-action (CTA)**

### **Steps:**

1. The user enters **Brand Name, Product Description, and Target Audience**.
2. Selects a preferred **tone** (Exciting, Professional, or Casual).
3. Clicks **Generate Copy**.
4. The app sends the request to **Groq Cloud's LLaMA API**, processes the response, and displays the AI-generated marketing content.

## Additional Features 🔥

✅ **Customizable Tone Selection** – Users can choose between different writing styles to match their brand identity.  
✅ **Secure API Integration** – Uses environment variables (`.env`) to protect API credentials.  
✅ **User-Friendly Interface** – Built with Streamlit for a seamless and interactive experience.  
✅ **Scalable & Efficient** – Uses LLaMA-3 AI model to generate high-quality, engaging content quickly.  
✅ **Optimized Error Handling** – Displays alerts if required inputs are missing and logs API responses for debugging.  

## Setup & Installation 🛠️

1️⃣ Clone the Repository
git clone https://github.com/harshdeepsinh8/AI-Marketing-Copy-Generator.git
cd AI-Marketing-Copy-Generator

2️⃣ Set API Key
GROQ_API_KEY=your-api-key

3️⃣ Run the Streamlit App
streamlit run app.py

## Tech Stack 🛠️

- **Programming Language:** Python  
- **Frameworks & Libraries:** Streamlit, Requests, dotenv  
- **AI Model:** Groq LLaMA-3 (via Groq Cloud API)  
- **Backend:** Python-based API calls to Groq  
- **Deployment:** Local system (can be extended to cloud hosting)  
- **Security:** Uses `.env` for API key management  
