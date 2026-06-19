import os

from modules.speak import speak

def execute(command):

    if "chrome" in command:

        speak("Opening Chrome")

        os.system("start chrome")

    elif "notepad" in command:

        speak("Opening Notepad")

        os.system("notepad")

    elif "hello" in command:

        speak("Hello Vishnu")

    elif "your name" in command:

        speak("My name is Jarvis")

    else:

        speak("I don't know that command yet.")