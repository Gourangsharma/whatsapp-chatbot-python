import pyautogui
import time
import pyperclip
import requests
import json
import re
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

MODEL = "deepseek/deepseek-chat-v3-0324:free"

    
pyautogui.click(938, 740)
time.sleep(1)  

while True:
    time.sleep(5)
    
    pyautogui.moveTo(510,188)
    pyautogui.dragTo(1303, 646, duration=2.0, button='left')  

    
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1) 
    pyautogui.click(919, 424) 

        
    chat_history = pyperclip.paste()

        
    print(chat_history)

      # 🔹 Extract last sender and message using regex
    matches = re.findall(r"\[\d{1,2}:\d{2} [ap]m, \d{1,2}/\d{1,2}/\d{4}\] (.*?): (.*)", chat_history)

    if not matches:
        print("No valid messages found. Waiting...")
        continue

    last_sender, last_message = matches[-1]
    print(f"Last sender: {last_sender}")

    # 🔸 Check if last message is from you
    if "gourang" in last_sender.lower():
        print("Message is from you. Skipping response...")
        continue

    print("Message is from someone else. Preparing response...")



    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",  # Required
        "X-Title": "Jarvis"                  # Optional
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a person named Gourang who speaks Hindi as well as English. "
                    "you are from India. You analyze chat history and respond like Gourang."
                    "Do not simulate typing or say 'Gourang is typing'. "
                    "Just answer directly with short messages in a natural way"
                )
            },
            {
                "role": "user",
                "content": chat_history
            }
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)


    result = response.json()

    if "error" in result:
        print("Error:", result["error"]["message"])
        continue  # Skip this loop and try again

# Check if 'choices' exists in response
    if "choices" not in result:
        print("Unexpected response:", result)
        continue

    response=(result["choices"][0]["message"]["content"])

    pyperclip.copy(response)

    pyautogui.click(663,681)
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    pyautogui.press('enter')
