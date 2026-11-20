
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("GEMINI_API_KEY")

print("Kalit topildimi:", bool(api_key))
print("Kalit uzunligi:", len(api_key) if api_key else 0)
print("Bo'sh joy bormi:", api_key != api_key.strip() if api_key else False)

if not api_key:
    raise SystemExit("API kalit .env faylida topilmadi!")

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction="""
        Your name is Salazar Slytherin.
        You are a personal AI assistant.

        Your primary language is Uzbek.
        You also speak English, Russian and Turkish.
        Respond in the language the user chooses.

        Personality:
        Intelligent, calm, strategic, elegant,
        respectful and slightly mysterious.

        Answer questions clearly and accurately.
        Never invent facts when uncertain.
        Admit when you do not know something.
        """
    )
)

print("🐍 SALAZAR AI")
print("Salazar: Assalomu alaykum. Men Salazar.")
print("Salazar: Sizga qanday yordam bera olaman?")

while True:
    message = input("\nYou: ").strip()

    if message.lower() in ["exit", "quit", "chiqish"]:
        print("Salazar: Xayr. Yana ko'rishguncha!")
        break

    if not message:
        continue

    
    try:
        response = chat.send_message(message)
        print("\nSalazar:", response.text or "Javob olinmadi.")

    except Exception as error:
        print("\nSalazar: Ulanishda xatolik yuz berdi.")
        print("Xatolik turi:", type(error).__name__)
        print("Xatolik kodi:", getattr(error, "code", "Noma'lum"))
        print("Xatolik xabari:", getattr(error, "message", "Noma'lum"))
