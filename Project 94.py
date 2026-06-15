num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
op=input("Enter operator:")
if (op=="+"):
    print(f"The sum of {num1} and {num2} is {num1+num2}")
elif (op=="-"):
    print(f"The subtraction of {num1} and {num2} is {num1-num2}")
elif (op=="*"):
    print(f"The product of {num1} and {num2} is {num1*num2}")
elif (op=="/"):
    print(f"The division of {num1} and {num2} is {num1/num2}")
else:
    print("Please enter a valid operator like +,-,/,*")
    