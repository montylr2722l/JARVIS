from datetime import datetime
from modules.speak import speak

def greet():

    hour = datetime.now().hour

    if hour < 12:
        speak("Good Morning Vishnu")

    elif hour < 18:
        speak("Good Afternoon Vishnu")

    else:
        speak("Good Evening Vishnu")

    speak("Jarvis is online.")