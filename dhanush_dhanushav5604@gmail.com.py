import pyttsx3
import webbrowser
import speech_recognition as sr
import sys

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def open_website(self, website_url, website_name):
        self.speak(f"Opening {website_name}")
        webbrowser.open(website_url)
        sys.exit()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            return self.recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError as e:
            print(f"Error connecting to Google Speech Recognition service; {e}")
            return ""

    def greet_user(self):
        self.speak("Hello! How can I assist you today?")

    def handle_hello(self):
        self.speak("Hi there! It's so nice to see you again.")

    def handle_open_command(self, command):
        websites = {
            "instagram": "https://www.instagram.com/",
            "facebook": "https://www.facebook.com/",
            "twitter": "https://twitter.com/",
            "youtube": "https://www.youtube.com/",
            "notepad": "https://www.notepad.com/"
        }

        for name, url in websites.items():
            if name in command:
                self.open_website(url, name.capitalize())
                break
        else:
            self.speak("I'm not sure which website to open. Can you please specify?")

    def handle_goodbye(self):
        self.speak("Goodbye! Have a great day.")
        sys.exit()

    def handle_unrecognized_command(self):
        self.speak("I'm not sure how to help with that. Can you please clarify?")

    def run(self):
        self.greet_user()

        while True:
            command = self.listen()
            if command:
                print(f"User said: {command}")

                if "hello" in command:
                    self.handle_hello()
                elif "open" in command:
                    self.handle_open_command(command)
                elif "goodbye" in command:
                    self.handle_goodbye()
                else:
                    self.handle_unrecognized_command()

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
