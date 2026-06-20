import os
import webbrowser

from datetime import datetime

from modules.speak import speak
from modules.logger import log_command


def execute(command):

    log_command(command)

    if "hello" in command:

        speak("Hello Vishnu")

    elif "your name" in command:

        speak("My name is Jarvis")

    elif "chrome" in command:

        speak("Opening Chrome")

        os.system("start chrome")

    elif "notepad" in command:

        speak("Opening Notepad")

        os.system("notepad")

    elif "google" in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")

    elif "youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

    elif "visual studio code" in command or "vs code" in command:

        speak("Opening Visual Studio Code")

        os.system("code")

    elif "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current_time}")

    elif "date" in command:

        current_date = datetime.now().strftime("%d %B %Y")

        speak(f"Today's date is {current_date}")

    else:

        speak("I do not know that command yet.")