import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ai_process(command):
    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.Chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def process_command(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif command.startswith("play"):
        song = command.replace("play", "").strip()
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find {song} in your library.")
    else:
        response = ai_process(command)
        speak(response)

def listen_for_command(prompt=""):
    if prompt:
        speak(prompt)
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
            return recognizer.recognize_google(audio)
        except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError):
            speak("Sorry, I didn't catch that.")
            return None

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("Waiting for wake word...")
        wake_word = listen_for_command()
        if wake_word and wake_word.lower() == "jarvis":
            speak("Yes?")
            user_command = listen_for_command("What can I do for you?")
            if user_command:
                process_command(user_command)