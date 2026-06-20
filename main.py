from modules.listen import listen
from modules.speak import speak
from modules.greet import greet
from modules.commands import execute

greet()

while True:

    wake_word = listen()

    if "exit" in wake_word:
        speak("Goodbye Vishnu")
        break

    if "jarvis" in wake_word:

        speak("Yes Vishnu")

        command = listen()

        if command:

            if "exit" in command:
                speak("Goodbye Vishnu")
                break

            execute(command)