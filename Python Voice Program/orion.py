import pyttsx3
import speech_recognition as sr
import webbrowser



def speck(txt):
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()
speck("Zain is Zain")

def process_command(c):
    if "open google" in c.lower():
        speck("opening")
        webbrowser.open("https://google.com")
if __name__ == "__main__":
    recognizer = sr.Recognizer()

    def listen():
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            print("Listening...")
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            if "orion" in text.lower():
                speck("Yes")
                speck("Listening for a command...")
                print("Listening for a command...")
            
                audio = recognizer.listen(mic)
                command_text = recognizer.recognize_google(audio)
                print(f"Command: {command_text}")
                
                # Process the recognized command
                process_command(command_text)
            


    while True:
        listen()
