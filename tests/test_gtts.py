from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")  # Or use "mpg321 output.mp3" 

# Example usage:
speak("Hello, this is a test using Google Text-to-Speech.")