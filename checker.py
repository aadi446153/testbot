import requests
import time
import os

BOT_TOKEN = os.environ.get("8619034589:AAFAkoD6Jgn1sWtx6OQlt9D3-vIbxJbUV-k")
CHAT_ID = os.environ.get("-5026711093")

URL = "https://shop.royalchallengers.com/ticket"
KEYWORD = "SRH"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

def check_site():
    try:
        response = requests.get(URL, timeout=10)
        content = response.text.upper()

        if KEYWORD in content:
            send_telegram("🚨 SRH tickets detected!\nhttps://shop.royalchallengers.com/ticket")
            return True
        else :
            send_telegram("No Tickets Found yet")
            

    except Exception as e:
        print("Error:", e)

    return False


while True:
    print("Checking...")
    found = check_site()

    if found:
        break   # stop after success

    time.sleep(31)  # check every 60 sec
