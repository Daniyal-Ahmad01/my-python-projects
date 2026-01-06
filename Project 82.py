def get_even(n):
    for i in range(1,n):
        if i%2==0:
            yield i
a=get_even(int(input("Enter your number:")))
for i in a:
    print(i)