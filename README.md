# 🤖 WhatsApp ChatBot using Python & OpenRouter API

This project is a Python automation bot that reads messages from WhatsApp Web and replies using the OpenRouter language model API.

---

##  Features
- Detects and reads the latest message from WhatsApp Web
- Uses OpenRouter API (DeepSeek model) to generate human-like replies
- Automatically pastes and sends the message
- Acts like a personalized bilingual chatbot (Hindi + English)

---

## 🛠️ Tech Stack
- Python
- OpenRouter API
- pyautogui
- pyperclip
- requests
- python-dotenv

---

##  Project Structure
```
whatsapp-chatbot-python/
│
├── chatbot.py # Main script
├── .env # Contains API key (not uploaded)
├── .gitignore # Hides .env and cache
├── requirements.txt # Required libraries
└── README.md # Project overview---

```
##  Setup Instructions

1. **Clone the repository** or download the code manually.

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Create a .env file in the same folder and add your OpenRouter API key:**
   
   ```bash
    API_KEY=your_openrouter_api_key_here
4. **Open WhatsApp Web in your browser and log in.**

5. **Adjust screen coordinates in bot.py to match your screen layout. You can use cursor.py for coordinates**

6. **Run the script:**

   ```bash
        python bot.py
---

##  Notes
- .env is excluded from GitHub using .gitignore — it contains private API key.
- pyautogui coordinates are hardcoded and may need adjustment for your screen.
- Keep WhatsApp Web open and visible while the script is running.
- This bot is intended strictly for educational and personal learning use.

---

## Author
Created by Gourang Sharma
Feel free to connect for collaboration, ideas, or questions.

---

## License
This project is licensed for educational and personal learning purposes only. Please do not misuse automation or APIs in a way that violates any platform's terms of service.

