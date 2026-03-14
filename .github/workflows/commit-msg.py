from datetime import datetime

military_hour = int(datetime.now().strftime("%H"))
current_hour = int(datetime.now().strftime("%I"))
am_pm = datetime.now().strftime("%p").lower()

if(military_hour > 5 and military_hour < 19):
    current_hour = f"☀️ {current_hour}{am_pm}"
else:
    current_hour = f"🌘 {current_hour}{am_pm}"

print(f"bot: {current_hour} - update banner")