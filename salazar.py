
from datetime import datetime

print("🐍 SALAZAR AI")
print("Welcome. I am Salazar Slytherin.")
print("Your personal AI assistant.")

while True:
    message = input("\nYou: ").strip()
    command = message.lower()

    if command in ["exit", "quit", "chiqish"]:
        print("Salazar: Until next time.")
        break
    elif "salom" in command or "hello" in command:
        print("Salazar: Salom! Sizga qanday yordam beraman?")
    elif "soat" in command or "time" in command:
        now = datetime.now().strftime("%H:%M")
        print(f"Salazar: Hozir soat {now}.")
    else:
        print("Salazar: Bu savolga javob berish uchun AI modelimni ulashimiz kerak.")
