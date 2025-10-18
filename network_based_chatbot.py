# Free Tier Limits (gemini-2.5-pro):
# • 5 requests per minute (RPM)
# • 25 requests per day
# • 1 million token context window
# • Access via Google AI Studio

# for long answers: 
# You are a helpful IT assistant. Diagnose this network problem and provide step-by-step troubleshooting instructions.\nProblem: {query}

import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

st.title("🤖 AI Network Fault Diagnosis Chatbot")
st.write("Describe your network issue, and I will suggest troubleshooting steps.")

user_input = st.text_area("💬 Your problem:")

network_keywords = [
    "network", "internet", "wifi", "wi-fi", "ethernet", "connection",
    "router", "modem", "dns", "ip", "ping", "latency", "speed",
    "packet", "signal", "bandwidth", "isp", "gateway"
]


knowledge_base = {
    "slow internet": [
        "1. Restart your router.",
        "2. Close apps consuming bandwidth.",
        "3. Check your internet speed using speedtest.net.",
        "4. If still slow, contact your ISP."
    ],
    "dns error": [
        "1. Check your DNS settings.",
        "2. Use Google DNS: 8.8.8.8 / 8.8.4.4.",
        "3. Flush DNS cache using 'ipconfig /flushdns' (Windows) or 'sudo systemd-resolve --flush-caches' (Linux)."
    ],
    "connection drop": [
        "1. Reboot your router.",
        "2. Check cables and WiFi signal strength.",
        "3. Update your network drivers.",
        "4. Contact your ISP if problem persists."
    ],
    "wifi not working": [
        "1. Ensure WiFi is turned on.",
        "2. Restart your router.",
        "3. Forget and reconnect to the WiFi network.",
        "4. Check if other devices are connecting properly."
    ]
}

def get_gemini_response(query):
    # url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-pro:generateContent?key={GEMINI_API_KEY}"
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"
    payload = {
        "contents": [
            {"parts": [{
                "text": (
                "You are a helpful Network Troubleshooting Assistant. Provide a short, step-by-step solution (4–5 steps max)"
                "Answer only questions related to computer networks (WiFi, routers, DNS, connectivity, etc.). "
                "If the question is not about networking, respond with: "
                "'⚠️ I can only answer questions related to network issues.'\n\n"
                "Answer format:\n"
                "Steps:\n"
                "1. <first step>\n"
                "2. <second step>\n"
                "3. <third step>\n"
                "4. <fourth step>\n\n"
                f"Problem: {query}"
            )
            }]}
        ]
    }
    try:
        response = requests.post(url, json=payload)
        result = response.json()
        if "error" in result:
            return f"⚠️ Gemini API Error:\n{result['error']['message']}"
        if "candidates" in result:
            return result['candidates'][0]['content']['parts'][0]['text']
        return "⚠️ Unknown response format from Gemini."
    except Exception as e:
        return f"⚠️ Exception: {str(e)}"

def get_solution(query):
    query_lower = query.lower()

    # Check if the query contains any network-related keyword
    if not any(keyword in query_lower for keyword in network_keywords):
        return "⚠️ This chatbot is designed to handle only **network-related problems**. Please ask network-related questions."

    # Check if it matches a known problem in the knowledge base
    for key in knowledge_base:
        if any(word in query_lower for word in key.split()):
            return "\n".join(knowledge_base[key])

    # Fallback to Gemini API
    return get_gemini_response(query)

if user_input.strip():
    solution = get_solution(user_input)
    st.markdown("## Suggested Solution: ")
    st.markdown(solution)
