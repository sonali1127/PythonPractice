import pyttsx3
import re
import os
import speech_recognition as sr
import datetime
import pyautogui
import time
import signal
import psutil
import webbrowser
import pyjokes
import pywhatkit as kitt
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Sona, your virtual assistant. How can I help you?")

def wakeWord():
    r = sr.Recognizer()
    attempts = 10
    speak("Say 'Sona' to wake me up.")
    for _ in range(attempts):
        with sr.Microphone() as source:
            print("Listening for wake word...")
            r.adjust_for_ambient_noise(source)
            try:
                audio = r.listen(source, timeout=10)
                audi = r.recognize_google(audio, language='en-in')
                print(f"Google Recognized: {audi}")
                if "sona" in audi.lower():
                    wishMe()
                    return True
                elif "exit" in audi.lower():
                    speak("Exiting. Goodbye!")
                    return False
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError:
                print("Network issue")
                speak("Network issue. Try again later.")
                return False
    speak("No wake word detected. Exiting...")
    return False

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source)
            audi = r.recognize_google(audio, language='en-in')
            print(f"User said: {audi}")
            return audi.lower()
        except sr.UnknownValueError:
            speak("I didn't catch that. Could you say it again?")
            return None
        except sr.RequestError:
            speak("Your network seems unstable. Please try again.")
            return None

todo_list = []

def add_to_list(task):
    todo_list.append(task)
    speak(f"Added {task} to your to-do list.")

def read_list():
    if not todo_list:
        speak("Your to-do list is empty.")
    else:
        speak("Your to-do list:")
        for task in todo_list:
            speak(task)

def take_note():
    speak("What should I write?")
    note = listen()
    if note:
        with open("notes.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {note}\n")
        speak("Note saved.")

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The time is {current_time}")
    print(f"Time: {current_time}")

def is_app_running(app_name):
    for process in psutil.process_iter(['name', 'pid']):
        if app_name.lower() in process.info['name'].lower():
            return process.info['pid']
    return None

def open_app_or_browser(app_name):
    if not app_name:
        speak("I couldn't identify the app. Could you repeat that?")
        return
    pyautogui.hotkey("win", "s")
    time.sleep(1)
    pyautogui.write(app_name)
    pyautogui.press("enter")
    time.sleep(5)
    if not is_app_running(app_name):
        speak(f"{app_name} is not installed. Opening in browser...")
        webbrowser.open(f"https://www.google.com/search?q={app_name}")

def close_app(app_name):
    found = False
    for process in psutil.process_iter(['name', 'pid']):
        if app_name.lower() in process.info['name'].lower():
            os.kill(process.info['pid'], signal.SIGTERM)
            found = True
    if found:
        speak(f"All instances of {app_name} have been closed.")
    else:
        speak(f"{app_name} is not running.")

def play_video(video_name):
    speak(f"Playing {video_name} on YouTube.")
    kitt.playonyt(video_name)

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)
    print(joke)

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
        print(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results. Can you be more specific?")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find anything on Wikipedia for that.")

# Main assistant loop
wake = wakeWord()
if wake:
    while True:
        query = listen()
        if not query:
            continue
        words = query.split()

        if "time" in query:
            tell_time()

        elif "open" in query:
            try:
                app_index = words.index("open") + 1
                if app_index < len(words):
                    app_name = words[app_index]
                    open_app_or_browser(app_name)
                else:
                    speak("Please specify what you want to open.")
            except (ValueError, IndexError):
                speak("Open what?")

        elif "close" in query or "exit" in query:
            try:
                close_index = words.index("close") if "close" in words else words.index("exit")
                if close_index + 1 < len(words):
                    app_name = words[close_index + 1]
                    close_app(app_name)
                else:
                    speak("Please specify what you want to close.")
            except (ValueError, IndexError):
                speak("Close what?")

        elif "play" in query:
            try:
                play_index = words.index("play") + 1
                if play_index < len(words):
                    play_name = ' '.join(words[play_index:])
                    play_video(play_name)
                else:
                    speak("Please specify what you want to play.")
            except (ValueError, IndexError):
                speak("Play what?")

        elif "note" in query:
            take_note()

        elif "joke" in query:
            tell_joke()

        elif "add to list" in query:
            task = query.replace("add to list", "").strip()
            if task:
                add_to_list(task)
            else:
                speak("What should I add to the list?")

        elif "what's on my list" in query or "read my list" in query:
            read_list()

        elif "what is" in query or "who is" in query or "tell me about" in query:
            query_clean = query.replace("what is", "").replace("who is", "").replace("tell me about", "").strip()
            if query_clean:
                search_wikipedia(query_clean)
            else:
                speak("What topic should I search on Wikipedia?")

        elif any(kw in query for kw in ["bye", "goodbye", "shut down", "exit assistant"]):
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("I'm not sure how to do that yet.")
