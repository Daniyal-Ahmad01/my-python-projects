import pyttsx3
engine=pyttsx3.init()
a=input("Enter your name:")
engine.say(f"Happy birthday to you {a} I am glad to see you.")
engine.runAndWait()