import pyaudio
import pyttsx3
import playsound
import subprocess
import processes
import speech_recognition as sr
from similarity import get_similarity_score

engine = pyttsx3.init()
TRIGGER = "wake up"


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        audio = r.listen(mic)
        said = ""
        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print(e)

    return said.lower()


def main():
    speak("Hello I'm C 3P O. Human Cyborg Relations. How may I serve you?")
    while True:
        text = listen()

        if text.count(TRIGGER) > 0:
            print("triggered")
            speak("Master Vedant!")

            text = listen()

            BROWSER_INTENT = ["google", "youtube", "meet", "teams", "reddit"]
            for intent in BROWSER_INTENT:
                if intent in text:
                    processes.open_websites(intent)
                    speak(f"launched {intent} ")

            text = listen()

            NOTE_INTENT = ["add to notes", "remember this"]
            for intent in NOTE_INTENT:
                if get_similarity_score(text, intent) > 0.5:
                    speak("What should I add?")
                    note = listen()
                    processes.add_notes(note)
                    speak(
                        "I've made a note of that. Perhaps the archives are complete."
                    )


main()
