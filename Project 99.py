def fib(f):
    if (f==1):
        return 1
    elif (f==0):
        return 0
    else:
        return fib(f-1)+fib(f-2)
print(fib(50))

