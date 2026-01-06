import time
a=int(time.strftime("%H",time.localtime()))
print(a)
if (a>=5 and a<=11):
    print("Good Morning!")
elif (a>11 and a<=16):
    print("Good Afternoon!")
elif (a>16 and a<=20):
    print("Good Evening!")
else:
    print("Good Night!")