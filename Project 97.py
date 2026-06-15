num=int(input("Enter a number: "))

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(f"The factorial of {num} with recursion is {fact(num)}")

a=1
for i in range(2,num+1):
    a=a*i
print(f"The factorial fo {num} with for loop is {a}")
