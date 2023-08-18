'''
import pyttsx3 

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak("")
'''

import pyttsx3
engine = pyttsx3.init()
answer=input("convert speech: ")
engine.say(answer)
engine.runAndWait()
