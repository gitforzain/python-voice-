import pyttsx3
import speech_recognition as sr
import webbrowser
import time

music = {
    "one": "https://www.youtube.com/watch?v=EKkzbbLYPuI",
    "2": "https://www.youtube.com/watch?v=UceaB4D0jpo",
    "3": "https://www.youtube.com/watch?v=MEg-oqI9qmw",
    "5": "https://www.youtube.com/watch?v=2fONEL2Udwo"
}

naats = {
    "it": "https://www.youtube.com/watch?v=2fONEL2Udwo",
    "6": "https://www.youtube.com/watch?v=UceaB4D0jpo",
    "7": "https://www.youtube.com/watch?v=MEg-oqI9qmw"
}

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def ProcessCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("opening google")
        print(" ")
        speak("Google Is Open Now")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("opening youtube")
        print( ) 
        print( )
        print( )
        print( )
        speak("Working")
        print()
        speak("Wait")
        speak("Wait")
        speak("youtube Is Open Now")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("opening facebook")
        speak("acebook Is Open Now")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("opening linkedin")
        speak("linkedin Is Open Now")
    elif "open search engine" in c.lower():
        webbrowser.open("https://google.com")
        speak("opening search engine")
        speak("engine Is Open Now")
    
    elif c.lower().startswith("play"):  # Check if the command starts with "play"
        song = c.lower().replace("play ", "").strip()  # Remove "play " from the command to get the song name
        link = music.get(song)  # Try to get the song link from the music dictionary
        if link:  # If the song is found (link is not None)
            webbrowser.open(link)  # Open the song in the web browser
        else:
            speak("Song not found")  # Speak if the song isn't found
    
    elif "play song" in c.lower():
        webbrowser.open("https://www.youtube.com/watch?v=EKkzbbLYPuI")
        speak("opening google")
    elif "open chat" in c.lower():
        webbrowser.open("https://chatgpt.com/")
        speak("opening chat GPT")
    elif "what is time now" in c.lower():
        t = time.strftime("%I:%M %p")
        print(t)
        speak(t)
    elif c.lower().startswith("get"):
        nat = c.lower().replace("get ", "").strip()
        link = naats.get(nat)
        if link:
            webbrowser.open(link)
            speak("opening")

        else:
            speak("This is not reachable for me")

if __name__ == "__main__":
    speak("Ke kam E")

    while True:
        try:
            with sr.Microphone() as source:
                # Reduce ambient noise for better recognition
                recognizer.adjust_for_ambient_noise(source, duration=1)

                speak("i am Listening now")
                print("Listening....")
                audio = recognizer.listen(source)

                # Recognize the speech
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")

                # Check if the user said "Hey Jarvis"
                if "hey jarvis" in text.lower():
                    speak("Yes")
                    speak("Listening for a command...")
                    print("Listening for a command...")

                    # Listen again for the command after "Hey Jarvis"
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    # Process the command
                    ProcessCommand(command)
                else:
                    # Process any other commands that don't start with "Hey Jarvis"
                    ProcessCommand(text)

        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
        except sr.RequestError as e:
            speak(f"Could not request results; {e}")
        except Exception as e:
            speak(f"Error: {e}")