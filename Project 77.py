import pyttsx3
engine=pyttsx3.init()
a=input("Enter your sentence:")
engine.say(a)
engine.runAndWait()