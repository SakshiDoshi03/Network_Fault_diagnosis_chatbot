**AI Network Fault Diagnosis Chatbot**

**Description**

The AI Network Fault Diagnosis Chatbot is a Streamlit application designed to help users quickly diagnose and troubleshoot common network and internet connectivity issues.

It operates using a dual-layer approach:
- Local Knowledge Base: It first checks the user's query against a small, pre-defined knowledge base for instant answers to common problems (e.g., "slow internet," "DNS error").

- Gemini API Fallback: If the query is not found in the local database or is more complex, it leverages the Gemini API (gemini-2.5-flash) to generate a concise, step-by-step troubleshooting guide, ensuring every network-related query receives a helpful, focused response.

**Features**

- Dual-Layer Diagnosis: Fast responses for common issues, intelligent generation for complex ones.
- Gemini-Powered Assistance: Utilizes the Gemini model for contextual, network-specific troubleshooting steps.
- Input Validation: Ensures the bot only responds to network-related questions.
- Simple Interface: Built with Streamlit for a clean, user-friendly web interface.

**Prerequisites**

Before running the application, ensure you have the following installed:
- Python 3.8+
- A Gemini API Key

**Installation**
Clone the repository (or save the file locally):
- git clone <your-repo-link>
- cd <your-project-directory>


Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


**Install the required Python packages:**
The application uses streamlit, requests, and python-dotenv.

- pip install streamlit requests python-dotenv


**API Key Setup (Gemini)**

This application requires your Gemini API Key to access the large language model features.
- Obtain a Key: Get your API key from Google AI Studio.
- Create .env file: In the root directory of your project, create a new file named .env.
- Add the key: Add your API key to the .env file in the following format:
- GEMINI_API_KEY="YOUR_API_KEY_HERE"


The application will automatically load this key upon startup.

**How to Run**

- After setting up the environment and API key, run the application using Streamlit:

- streamlit run your_script_name.py

(Replace your_script_name.py with the name of your Python file, e.g., app.py)

The application will open in your default web browser (usually at http://localhost:8501).

**Troubleshooting Logic**
The core diagnostic logic is housed in the get_solution function:
- Network Check: It first verifies if the user's query contains any key network terms (wifi, router, dns, connection, etc.). If not, it rejects the query.
- Knowledge Base Lookup: It iterates through the hardcoded knowledge_base dictionary (e.g., checking for "slow internet" or "dns error"). If a match is found, it returns the local, predefined solution immediately.
- API Call: If no local match is found, it falls back to calling the Gemini API (gemini-2.5-flash). The API call uses a specific System Instruction to constrain the model, ensuring it acts as a "Network Troubleshooting Assistant" and provides a short, numbered list of steps (4-5 steps max).