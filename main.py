from modules.listen import listen
from modules.speak import speak
from modules.commands import execute
from modules.greet import greet

greet()

while True:

    command = listen()

    if command:

        if "exit" in command:
            speak("Goodbye Vishnu")
            break

        execute(command)