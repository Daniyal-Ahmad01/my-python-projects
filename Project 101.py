class CustomError(Exception):
    pass
try:
    a=int(input("Enter a number:"))
except CustomError:
    print("MY CUSTOM ERROR HAS OCCURED!")
if a<0 or a>100:
        raise(CustomError("Age cannot be that unreal"))