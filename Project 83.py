import time
import pyttsx3
engine=pyttsx3.init()
for i in range(n:=int(input("Enter a number:")),0,-1):
    engine.say(str(i))
    engine.runAndWait()
    print(i)
    time.sleep(1)