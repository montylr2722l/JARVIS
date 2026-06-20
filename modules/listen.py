import speech_recognition as sr

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except Exception:

        return ""